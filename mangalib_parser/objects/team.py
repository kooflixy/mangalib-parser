from mangalib_parser.objects.main_object import MainObject
from mangalib_parser.objects.team_member import TeamMember
from mangalib_parser.settings.logging import do_log
from mangalib_parser.utils.decorators import *
from mangalib_parser.utils import generators, converters, parser
from mangalib_parser.data import models


class Team(MainObject):
    def __init__(self, id: int, autparse: bool=True):    #creates in User.get_user_info()
        self.id: int = id
        self.model: models.Model = models.TEAM
        self.url: str = self.get_url()

        self.name: str = None
        self.discord: str = None
        self.vk: str = None
        self.website: str = None
        
        if autparse:
            self.get_team_info()
    
    def __str__(self):
        return f'Team({self.id})'

    @do_log
    def get_url(self) -> str:
        return 'https://' + self.site.domain + '/ru/' + self.model.model + '/' + self.id

    @do_log
    def get_team_info(self):
        '''Parses and returns more info about team'''
        url = generators.generate_team_parsing_url(self.id)
        team = parser.get_json_response(url, self.site.headers, None)
        team = team['data']

        self.name = team['name']
        # self.description = ''
        # if team['description']:
        #     descrip = team['description']['content']
        #     for str_ in descrip:
        #         if str_['type'] == 'hardBreak':
        #             self.description += '\n'
        #         elif 'text' in str_:
        #             self.description += str_['text']
        #         if 'marks' in str_:
        #             for item in str_['marks']:
        #                 self.description += item
        
        self.discord = team['discord']
        self.vk = team['vk']
        self.website = team['website']
    


    @convert_to_class(converters.to_team_member)
    @do_log
    def get_members(self, as_json: bool=False) -> list[TeamMember]:
        '''Sends members of translater team
        :param as_json: Is responsible for whether to translate the json response into the class. // Отвечает за то, переводить ли json ответ в соответствующий класс.
        '''

        url = generators.generate_team_members_parsing_url(self.slug_url)
        response = parser.get_json_response(url, self.site.headers, None)['data']
        return response, as_json