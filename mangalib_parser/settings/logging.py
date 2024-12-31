import logging
import time

logging.basicConfig(
    level=logging.INFO, filename='log.log', filemode='a', encoding='utf-8',
    format='%(asctime)s %(levelname)s %(message)s'
)

def do_log(func):
    def wrapped(*args, **kwargs):
        start_time = time.time()
        # logging.info(f'{str(args[0])}.{func.__name__} started')

        res = func(*args, **kwargs)

        lead_time = time.time() - start_time
        if args:
            cl = str(args[0])
            cl = cl[:50] if len(cl)>=50 else cl
        else: cl=''
        
        logging.info(f'{cl}.{func.__name__} was completed in {lead_time}s')
        return res
    return wrapped