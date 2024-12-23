class Status:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

ALL = Status(0, 'Все')
READING = Status(1, 'Читаю')
IN_PLANS = Status(2, 'В планах')
ABADONED = Status(3, 'Брошено')
READ = Status(4, 'Прочитано')
FAVORITES = Status(5, 'Любимые')



IDS = [0,1,2,3,4,5,]
STATUSES_LIST = [ALL, READING, IN_PLANS, ABADONED, READ, FAVORITES]
def get_status_by_id(id:int):
    index = IDS.index(id)
    return STATUSES_LIST[index]