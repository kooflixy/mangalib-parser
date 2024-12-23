class Status:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

# manga
ALL = Status(0, 'Все')
READING = Status(1, 'Читаю')
IN_PLANS = Status(2, 'В планах')
ABADONED = Status(3, 'Брошено')
READ = Status(4, 'Прочитано')
FAVORITES = Status(5, 'Любимые')

# anime
WATCHING = Status(21, 'Смотрю')
PLANNED = Status(22, 'Запланировано')
ANI_ABADONED = Status(23, 'Брошено')
VIEWED = Status(24, 'Просмотрено')
ANI_FAVORITES = Status(25, 'Любимые')
REWATCHING =  Status(26, 'Пересматриваю')
POSTPONED = Status(27, 'Отложено')


STATUSES_LIST = [
    ALL, READING, IN_PLANS, ABADONED, READ, FAVORITES, 
    WATCHING, PLANNED, ANI_ABADONED, VIEWED, ANI_FAVORITES, REWATCHING, POSTPONED,
]
IDS = [
    0,1,2,3,4,5,
    21,22,23,24,25,26,27,
]
def get_status_by_id(id:int) -> Status:
    index = IDS.index(id)
    return STATUSES_LIST[index]