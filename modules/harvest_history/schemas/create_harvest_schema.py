from pydantic import BaseModel

class CreateHarvestSchema(BaseModel):
    """ Define os dados para cadastrar uma nova colheita
    """
    date:str = ""
    total_production:int = 30
    field:int = 1
    user:str = "micael@gmail.com"
