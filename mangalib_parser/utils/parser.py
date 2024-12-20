import requests
from mangalib_parser.utils.decorators import retry


@retry
def get_json_response(url: str, headers: dict, params: dict) -> dict:
    '''Get json response from ONLY one page // Получает json ответ от ТОЛЬКО 1 страницы
    :param url: Url to which the request is sent // Ссыылка, по которой воспроизводится get-запрос
    :param headers: Headers for get-requests are stored in the specified class site(you can import them from mangalib_parser/data/sites.py) // Хедеры для get-запроса, хранящиеся в указанном в классе сайте(Вы можете импортировать их из mangalib_parser/data/sites.py)
    :param params: Parameters for get-requests // Параметры для get-запроса.
    '''

    response = requests.get(url=url, headers=headers, params=params)
    return response.json()



def get_pages(url, headers, params, page=0, count=0, max_count=None):
    if max_count==0:
        return []
    
    page+=1
    params['page'] = page
    response = get_json_response(url, headers, params)
    result = response['data']
    if max_count:
        count+=len(result)
        if count<max_count:
            if response['links']['next']:  #Parses the next page if it exists // Парсит следующую страницу, если она существует
                result+=get_pages(url, headers, params, page, count, max_count)
        else:
            difference = count-max_count
            if difference!=0:
                a = []
                b = 0
                kolvo = len(result)-difference
                for item in result:
                    a.append(item)
                    b+=1
                    if b >=kolvo:
                        return a
    else:
        if response['links']['next']:  #Parses the next page if it exists // Парсит следующую страницу, если она существует
            result+=get_pages(url, headers, params, page)
    return result