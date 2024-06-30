from pydantic import BaseModel

class ListFieldsByUserQuerySchema(BaseModel):
    """ Define o que é necessário ser inserido para ser retornado a lista de talhões por usuário.
    """
    user:str = ''