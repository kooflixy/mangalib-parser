from datetime import datetime
from mangalib_parser.objects.main_object import MainObject
from mangalib_parser.settings.logging import do_log


class Friend(MainObject):
    def __init__(self, user_id: int, **kwargs):
        self.user_id: int = user_id
        
        self.comment: str = None
        self.created_at: datetime = None
        self.status: dict = None
        self.__dict__.update(kwargs)
    
    def __str__(self):
        return f'Friend({self.user_id})'