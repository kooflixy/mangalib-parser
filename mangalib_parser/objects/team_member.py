from mangalib_parser.objects.main_object import MainObject



class TeamMember(MainObject):
    def __init__(self, user_id: int, **kwargs):
        self.user_id = user_id

        self.roles: list = None
        self.permissions: list = None
        self.team_id: int = None

        self.__dict__.update(kwargs)
    
    def __str__(self):
        return f'TeamMember({self.id})'