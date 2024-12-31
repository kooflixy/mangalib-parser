from mangalib_parser.settings.logging import do_log
from mangalib_parser.utils import converters, generators, parser
from mangalib_parser.utils.decorators import *
from mangalib_parser.objects.main_object import MainObject
from mangalib_parser.objects.team import Team
from mangalib_parser.data import sites, statuses, models, level
from mangalib_parser.data.sites import Site
from mangalib_parser.data.statuses import Status
from mangalib_parser.data.level import Level

from datetime import datetime


class User(MainObject):
    def __init__(self, id: int, autoparse: bool=True, **kwargs):
        self.id: int = id
        self.model: models.Model = models.USER
        self.url = generators.get_user_profile_url(self)

        self.username: str = None
        self.about: str = None
        self.last_online_at: datetime = None
        self.created_at: datetime = None
        self.level: level.Level = None
        self.teams: list[Team] = None
        self.__dict__.update(kwargs)
        if autoparse:
            self.get_user_info()

    def __str__(self):
        return f'User({self.id})'


    @do_log
    def get_user_info(self):
        '''Parses and returns more info about user'''

        url = generators.generate_user_profile_parsing_url(self.id)
        profile = parser.get_json_response(url, self.site.headers, {'fields[]':['background', 'roles', 'points', 'ban_info', 'gender', 'created_at', 'about', 'teams',]})
        profile = profile['data']

        self.username = profile['username']
        self.about = profile['about']
        self.last_online_at = datetime.strptime(profile['last_online_at'][:-8], "%Y-%m-%dT%H:%M:%S") if 'last_online_at' in profile else None
        self.created_at = datetime.strptime(profile['created_at'][:-8], "%Y-%m-%dT%H:%M:%S")
        self.level = Level(
            total_points = profile['points_info']['total_points'],
            level = profile['points_info']['level'],
            max_level_points = profile['points_info']['max_level_points'],
            current_level_points = profile['points_info']['current_level_points'],
            point_percent_progress = profile['points_info']['point_percent_progress'],
        )
        self.teams = [Team(id=team['id']) for team in profile['teams']]
    

    @convert_to_class(converters.to_bookmark)
    @do_log
    def get_bookmarks(self, sort_by='name', sort_type='desc', status: Status=statuses.ALL, site:Site=sites.MANGALIB, as_json:bool=False, count:int=None) -> dict:
        r'''Sends user's bookmark from the selected site
        :param sort_by: Sort selection by critetion. // Выбор сортировки по критерию.
                        Can take values like this: // Может принимать такие значения:
                            'name' - Sort by english alphabet // Сортировка по английскому алфавиту
                            'rus_name' - Sort by russian alphabet // Сортировка по русскому алфавиту
                            'created_at' - Sort by date added // Сортировка по дате добавления
                            'updated_at' - Sort by reading date // Сортировка по дате чтения
                            'last_chapter_at' - Sort by chapter update date // Сортировка по дате обновления глав
        :param sort_type: Select sort order. // Выбор порядка сортировки.
                        Can take values like this: // Может принимать такие значения:
                            'desc' - Sort in descending // Сортировка по убыванию
                            'asc' - Sort in ascending // Сортировка по возрастанию
        :param status: Folder whose bookmarks will be parsed (Reading, Read, etc.). Imported from mangalib_parser.data.statuses // Папка, из которой будут парситься закладки(Читаю, Прочитано и т.д.). Импортируются из mangalib_parser.data.statuses
        :param site: Site from which bookmarks will be parsed. Imported from mangalib_parser.data.sites // Сайт, с которого будут парситься закладки. Импортируется из mangalib_parser.data.sites
        :param as_json: Is responsible for whether to translate the json response into the class. // Отвечает за то, переводить ли json ответ в соответствующий класс.
        :param count: How many bookmarks to return. // Сколько возвратить закладок.
        
        This method returns 'as_json' so that the @convert_to_class checks whether to convert the json response to the appropriate class // Этот метод возвращает 'as_json', чтобы @convert_to_class проверил, переводить ли json ответ в соответствущий класс
        '''

        url = generators.generate_user_bookmarks_parsing_url()
        response = self.parse(url=url, count=count, site=site, sort_by=sort_by, sort_type=sort_type, user_id=self.id, status=status.id)
        return response, as_json


    @convert_to_class(converters.to_comment)
    @do_log
    def get_comments(self, sort_by='id', sort_type='desc', as_json:bool=False, count:int=None) -> dict:

        r'''Sends user's comments
        :param sort_by: Sort selection by critetion. // Выбор сортировки по критерию.
                        Can take values like this: // Может принимать такие значения:
                            'id' - Sort by time // Сортировка по времени
                            'votes' - Sort by rating // Сортировка по рейтингу
        :param sort_type: Select sort order. // Выбор порядка сортировки.
                        Can take values like this: // Может принимать такие значения:
                            'desc' - Sort in descending // Сортировка по убыванию
                            'asc' - Sort in ascending // Сортировка по возрастанию
        :param as_json: Is responsible for whether to translate the json response into the class. // Отвечает за то, переводить ли json ответ в соответствующий класс.
        :param count: How many comments to return. // Сколько возвратить комментариев.
        
        This method returns 'as_json' so that the @convert_to_class checks whether to convert the json response to the appropriate class // Этот метод возвращает 'as_json', чтобы @convert_to_class проверил, переводить ли json ответ в соответствущий класс
        '''

        url = generators.generate_user_comments_parsing_url(user_id = self.id)
        response = self.parse(url=url, count=count, sort_by=sort_by, sort_type=sort_type)
        return response, as_json
    

    @convert_to_class(converters.to_friend)
    @do_log
    def get_friends(self, as_json:bool=False, count:int=None) -> dict:
        
        r'''Sends user's friends
        :param as_json: Is responsible for whether to translate the json response into the class. // Отвечает за то, переводить ли json ответ в соответствующий класс.
        :param count: How many friends to return. // Сколько возвратить друзей.
        
        This method returns 'as_json' so that the @convert_to_class checks whether to convert the json response to the appropriate class // Этот метод возвращает 'as_json', чтобы @convert_to_class проверил, переводить ли json ответ в соответствущий класс
        '''
        url = generators.generate_user_friends_parsing_url()
        response = self.parse(url=url, count=count, user_id=self.id, status=1)
        return response, as_json