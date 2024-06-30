from pydantic import BaseModel

class CreateFieldSchema(BaseModel):
    """ Define os dados para cadastrar um talhão
    """
    area:float = 20
    planting:str = "soja"
    user:str = "micael@gmail.com"
