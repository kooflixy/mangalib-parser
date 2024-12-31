class Status:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
    
    def __str__(self):
        return self.name

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
def get_status_by_id(id:int) -> Status:
    for status in STATUSES_LIST:
        if status.id == id:
            return status