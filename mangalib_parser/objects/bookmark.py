from datetime import datetime
from mangalib_parser.data import models, sites, statuses
from mangalib_parser.objects.main_object import MainObject


class Bookmark(MainObject):
    def __init__(self, **kwargs):
        
        self.chapter: int = None
        self.page: int = None
        self.status: statuses.Status = None
        self.created_at: datetime = None
        self.updated_at: datetime = None
        self.name: str = None
        self.rus_name: str = None
        self.slug_url: str = None
        self.site: sites.Site = None
        self.model: models.Model = None
        
        self.__dict__.update(kwargs)
        self.url: str = self.get_url()
    
    def __str__(self):
        return f'Bookmark({self.name})'