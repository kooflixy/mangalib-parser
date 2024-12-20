from mangalib_parser.data import sites
from mangalib_parser.utils import get_pages

class MainObject:
    
    site: sites.Site = sites.MANGALIB

    def parse(self, url: str, count, **params) -> dict:
        return get_pages(url=url, headers=self.site.headers, params=params, max_count=count)