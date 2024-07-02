from pydantic import BaseModel

class ProductivityMapQuerySchema(BaseModel):
    """ Define os dados necessários para buscar mapa de produtividade dos talhões.
    """
    user: str
