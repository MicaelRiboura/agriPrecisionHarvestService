from pydantic import BaseModel
from typing import List
from .productivity_field_schema import ProductivityFieldSchema

class ProductivityMapResponseSchema(BaseModel):
    """ Define como mapa de produtividade dos talhões é representado.
    """
    fields: List[ProductivityFieldSchema]