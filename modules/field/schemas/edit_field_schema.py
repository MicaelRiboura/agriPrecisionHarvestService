from pydantic import BaseModel

class EditFieldSchema(BaseModel):
    """ Define os dados para editar um talhão
    """
    id:int = 1
    area:float = 20
    planting:str = "feijão"
    user:str = "micael@gmail.com"