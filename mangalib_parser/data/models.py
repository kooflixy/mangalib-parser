class Model:
    def __init__(self, model: str, name: str):
        self.model = model
        self.name = name
    
    def __str__(self):
        return self.name

POST = Model('post', 'Пост')
CHAPTER = Model('chapter', 'Глава')
EPISODES = Model('episodes', 'Эпизод')
MANGA = Model('manga', 'Манга/Ранобе')
ANIME = Model('anime', 'Аниме')
USER = Model('user', 'Пользователь')
TEAM = Model('team', 'Команда')
COLLECTION = Model('collection', 'Коллекция')
REVIEW = Model('review', 'Отзыв')


MODELS_LIST = [MANGA, USER, TEAM, CHAPTER, POST, ANIME, EPISODES, COLLECTION, REVIEW]
def get_tmodel_by_model(model:str) -> Model:
    for tmodel in MODELS_LIST:
        if tmodel.model == model:
            return tmodel