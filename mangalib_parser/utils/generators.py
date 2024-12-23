from mangalib_parser.settings.settings import API_DOMEN

def add_protocol_and_domen(func):
    def wrapped(*args, **kwargs):
        path = func(*args, **kwargs)
        return 'https://' + API_DOMEN + path
    return wrapped


@add_protocol_and_domen
def generate_user_bookmarks_parsing_url() -> str:
    return f'/api/bookmarks'

@add_protocol_and_domen
def generate_user_comments_parsing_url(user_id: int) -> str:
    return f'/api/user/{user_id}/comments'

@add_protocol_and_domen
def generate_user_friends_parsing_url() -> str:
    return f'/api/friendship'
