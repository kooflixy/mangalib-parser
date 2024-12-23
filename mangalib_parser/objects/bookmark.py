from mangalib_parser.objects.main_object import MainObject


class Bookmark(MainObject):
    def __init__(self, **kwargs):
        self.__dict__ = kwargs
        self.url = self.get_url()