import time

from mangalib_parser.settings import settings
import logging


def retry(parsing_func):

    '''Waits and tries again if an incorrect response comes. // Ждет и пытается снова, если приходит некорректный ответ.'''

    def wrapped(*args, **kwargs):
        for try_ in range(1, settings.MAX_OF_ATTEMPTS+1):
            try:
                return parsing_func(*args, **kwargs)
            except Exception as ex:
                if try_ != settings.MAX_OF_ATTEMPTS:
                    logging.info(f'{try_} attempt to parse: {ex}')
                    time.sleep(settings.TIMEOUT_BETWEEN_REPETITIONS)
                else:
                    {'data': []}
    return wrapped




def convert_to_class(converting_func):
    def converting_check(main_func):

        def wrapped(*args, **kwargs):
            original_result: tuple = main_func(*args, **kwargs)    #main_func() -> tuple(response, as_json: bool)
            response = original_result[0]     #Give response // Передаем response

            if not original_result[1]:        #Checking whether to translate json into a class // Проверка, переводить ли json в класс
                response = converting_func(response)
            return response
        
        return wrapped
    return converting_check