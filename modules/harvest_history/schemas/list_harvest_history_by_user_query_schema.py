from pydantic import BaseModel

class ListHarvestHistoryByUserAndFieldQuerySchema(BaseModel):
    """ Define o que é necessário ser inserido para ser retornado a lista de histórico de colheitas por usuário.
    """
    field:int = 1
    user:str = ''