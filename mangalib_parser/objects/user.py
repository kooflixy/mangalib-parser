from mangalib_parser.utils import converters, generators
from mangalib_parser.utils.decorators import *
from mangalib_parser.objects.main_object import MainObject


class User(MainObject):
    def __init__(self, id: int, **kwargs):
        self.__dict__ = kwargs
        self.id = id
    

    @convert_to_class(converters.to_comment)
    def get_comments(self, sort_by='id', sort_type='desc', as_json:bool=False, count:int=None) -> dict:

        r'''Sends user's comments
        :param sort_by: Sort selection by critetion. // Выбор сортировки по критерию.
                        Can take values like this: // Может принимать такие значения:
                            'id' - Sort by time // Сортировка по времени
                            'votes' - Sort by rating // Сортировка по рейтингу
        :param sort_type: Select sort order. // Выбор порядка сортировки.
                          Can take values like this: // Может принимать такие значения:
                            'desc' - Sort in descending // Сортировка по убыванию
                            'votes' - Sort in ascending // Сортировка по возрастанию
        :param as_json: Is responsible for whether to translate the json response into the class. // Отвечает за то, переводить ли json ответ в соответствующий класс.
        :param count: How many comments to return. // Сколько возвратить комментариев.
        
        This method returns 'as_json' so that the @convert_to_class checks whether to convert the json response to the appropriate class // Этот метод возвращает 'as_json', чтобы @convert_to_class проверил, переводить ли json ответ в соответствущий класс
        '''

        url = generators.generate_user_comments_parsing_url(user_id = self.id)
        response = self.parse(url=url, count=count, sort_by=sort_by, sort_type=sort_type)
        return response, as_json
    
    @convert_to_class(converters.to_friend)
    def get_friends(self, as_json:bool=False, count:int=None) -> dict:
        
        r'''Sends user's friends
        :param as_json: Is responsible for whether to translate the json response into the class. // Отвечает за то, переводить ли json ответ в соответствующий класс.
        :param count: How many comments to return. // Сколько возвратить комментариев.
        
        This method returns 'as_json' so that the @convert_to_class checks whether to convert the json response to the appropriate class // Этот метод возвращает 'as_json', чтобы @convert_to_class проверил, переводить ли json ответ в соответствущий класс
        '''
        url = generators.generate_user_friends_parsing_url()
        response = self.parse(url=url, count=count, user_id=self.id, status=1)
        return response, as_json