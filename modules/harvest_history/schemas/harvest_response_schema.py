from pydantic import BaseModel

class HarvestResponseSchema(BaseModel):
    """ Define como um registro de colheita deve ser representado
    """
    id:int = 1
    date:str = '2024-06-01'
    total_production: int
    field: int
    user: str