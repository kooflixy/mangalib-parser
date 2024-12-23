class Site:
    def __init__(
        self,
        id: int,
        domain: str,
    ):
        self.id: int = id
        self.domain: str = domain
        self.headers: dict = {             #Headers for selected site // Хедеры для выбранного сайта
            'origin': 'https://' + self.domain,
            'referer': 'https://' + self.domain + '/',
            'site-id': str(self.id),
        }


MANGALIB = Site(1, 'mangalib.me')
SLASHLIB = Site(2, 'v2.slashlib.me')
RANOBELIB = Site(3, 'ranobelib.me')
HENTAILIB = Site(4, 'hentailib.me')
ANIMELIB = Site(5, 'anilib.me')


SITES_LIST = [MANGALIB, SLASHLIB, RANOBELIB, HENTAILIB, ANIMELIB]
IDS = [1,2,3,4, 5]

def get_site_by_id(id:int) -> Site:
    index = IDS.index(id)
    return SITES_LIST[index]