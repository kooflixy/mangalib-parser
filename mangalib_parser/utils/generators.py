from mangalib_parser.settings.settings import API_DOMEN

def add_protocol_and_domen(func):
    def wrapped(*args, **kwargs):
        path = func(*args, **kwargs)
        return 'https://' + API_DOMEN + path
    return wrapped


def get_user_profile_url(self):
    return 'https://' + self.site.domain + '/ru/' + self.model.model + '/' + str(self.id)


#for parsing

@add_protocol_and_domen
def generate_user_profile_parsing_url(user_id: int) -> str:
    return '/api/user/' + str(user_id)

@add_protocol_and_domen
def generate_user_bookmarks_parsing_url() -> str:
    return '/api/bookmarks'

@add_protocol_and_domen
def generate_user_comments_parsing_url(user_id: int) -> str:
    return f'/api/user/{user_id}/comments'

@add_protocol_and_domen
def generate_user_friends_parsing_url() -> str:
    return '/api/friendship'
