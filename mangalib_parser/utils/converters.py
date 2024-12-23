from mangalib_parser.objects.bookmark import Bookmark
from mangalib_parser.data import statuses, sites
from datetime import datetime

def to_bookmark(json: list) -> list[Bookmark]:
    result = []
    print(json)
    for bookmark in json:
        result.append(
            Bookmark(
                chapter = (bookmark['meta']['item_number'] if bookmark['meta'] else None),
                page = bookmark['progress'],
                status = statuses.get_status_by_id(bookmark['status']),
                created_at = datetime.strptime(bookmark['created_at'], '%Y-%m-%d %H:%M:%S'),
                updated_at = datetime.strptime(bookmark['updated_at'][:-8], "%Y-%m-%dT%H:%M:%S"),
                name = bookmark['media']['name'],
                rus_name = bookmark['media']['rus_name'],
                slug_url = bookmark['media']['slug_url'],
                site = sites.get_site_by_id(bookmark['media']['site']),
                model = bookmark['media']['model']
            )
    )
    return result

def to_comment(json: dict):
    # print('типа конвертировалос')
    return json

def to_friend(json: dict):
    # print('типа конвертировалос')
    return json