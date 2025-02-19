from pydantic import BaseModel

class ProductivityFieldSchema(BaseModel):
    """Define como um registro de mapa de produtividade dos talhões é representado.
    """
    field:int = 1
    planting:str = "Soja"
    average: int = 30
