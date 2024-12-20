class Site:
    def __init__(
        self,
        id: int,
        domen: str,
    ):
        self.id: int = id
        self.domen: str = domen
        self.headers: dict = {             #Headers for selected site // Хедеры для выбранного сайта
            'origin': 'https://' + self.domen,
            'referer': 'https://' + self.domen + '/',
        }


MANGALIB = Site(1, 'mangalib.me')
SLASHLIB = Site(2, 'v2.slashlib.me')
RANOBELIB = Site(3, 'ranobelib.me')
HENTAILIB = Site(4, 'hentailib.me')