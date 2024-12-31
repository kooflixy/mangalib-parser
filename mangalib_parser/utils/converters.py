from mangalib_parser.objects.bookmark import Bookmark
from mangalib_parser.objects.friend import Friend
from mangalib_parser.objects.team_member import TeamMember
from mangalib_parser.objects.comment import Comment
from mangalib_parser.data import statuses, sites, models
from datetime import datetime

from mangalib_parser.settings.logging import do_log

@do_log
def to_bookmark(json: list) -> list[Bookmark]:
    result = []
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
                model = models.get_tmodel_by_model(bookmark['media']['model']),
            )
    )
    return result

@do_log
def to_comment(json: dict) -> list[Comment]:
    result = []
    for comment in json:
        com = Comment(
            comment = comment['comment'],
            id = comment['id'],
            created_at = datetime.strptime(comment['created_at'][:-8], "%Y-%m-%dT%H:%M:%S"),
            user_id = comment['user']['id'],
            votes = [comment['votes']['down'], comment['votes']['up']],  #list[down, up]
            relation_type = models.get_tmodel_by_model(comment['relation_type']),
        )

        if not comment['relation']:
            result.append(com)
            continue
        
        if com.relation_type == models.CHAPTER:
            com.site = sites.get_site_by_id(comment['relation']['media']['site'])
            com.slug_url = comment['relation']['media']['slug_url']
            com.url = f'https://{com.site.domain}/ru/{com.slug_url}/read/v{comment['relation']['number_secondary']}/c{comment['relation']['number']}?bid={comment['relation']['branch_id']}&comment_id={com.id}&p={comment['post_page']}'
        
        elif com.relation_type == models.EPISODES:
            com.site = sites.get_site_by_id(comment['relation']['media']['site'])
            com.slug_url = comment['relation']['media']['slug_url']
            com.url = f'https://{com.site.domain}/ru/anime/{com.slug_url}/watch?episode={comment['relation']['id']}'

        elif com.relation_type == models.MANGA or com.relation_type == models.ANIME:
            sites.get_site_by_id(comment['relation']['site'])
            com.slug_url = comment['relation']['slug_url']
            com.url = f'https://{com.site.domain}/ru/{com.relation_type.model}/{com.slug_url}?comment_id={com.id}&section=comments'
        
        elif com.relation_type == models.POST:
            com.slug_url = comment['relation']['slug_url']
            com.url = f'https://{com.site.domain}/ru/news/{com.slug_url}?comment_id={com.id}'
        
        elif com.relation_type == models.COLLECTION:
            com.site = sites.get_site_by_id(comment['relation']['site_id'])
            com.slug_url = comment['relation']['id']
            com.url = f'https://{com.site.domain}/ru/collections/{com.slug_url}?comment_id={com.id}'
        
        elif com.relation_type == models.REVIEW:
            com.site = sites.get_site_by_id(comment['relation']['site_id'])
            com.url = f'https://{com.site.domain}/ru/reviews/{comment['relation']['id']}?comment_id={com.id}'
        
        result.append(com)
    return result

@do_log
def to_friend(json: dict) -> list[Friend]:
    result = []
    for friend in json:
        result.append(
            Friend(
                user_id = friend['user']['id'],
                comment = friend['comment'],
                created_at = datetime.strptime(friend['created_at'][:-8], "%Y-%m-%dT%H:%M:%S"),
                status = friend['status']
            )
    )
    return result

@do_log
def to_team_member(json: dict) -> list[TeamMember]:
    result = []
    for member in json:
        result.append(
            TeamMember(
                user_id = member['user']['id'],
                roles = member['roles'],
                permissions = member['permissions'],
                team_id = member['team_id'],
            )
    )
    return result