from datetime import datetime
from mangalib_parser.data import models, sites
from mangalib_parser.objects.main_object import MainObject


class Comment(MainObject):
    def __init__(self, comment: str, id: int, created_at: datetime, user_id: int, votes: list[int, int], relation_type: models.Model, **kwargs):
        self.comment = comment
        self.id = id
        self.created_at = created_at
        self.user_id = user_id
        self.votes = votes   #list[down, up]
        self.relation_type = relation_type
        self.slug_url: str|int = ''
        self.url: str = ''

        self.__dict__.update(kwargs)

    def __str__(self):
        return f'Comment({self.comment})'