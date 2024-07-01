from pydantic import BaseModel

class HarvestByIdAndFieldSchemaQuerySchema(BaseModel):
    """ Define os dados necessários para buscar um registro de colheita
    """
    id:int = 1
    user: str = ""