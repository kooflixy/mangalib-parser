class Model:
    def __init__(self, model: str):
        self.model = model

MANGA = Model('manga')
USER = Model('user')


MODELS_LIST = [MANGA, USER]
MODELS = ['manga', 'user']
def get_tmodel_by_model(model:str) -> Model:
    index = MODELS.index(id)
    return MODELS_LIST[index]