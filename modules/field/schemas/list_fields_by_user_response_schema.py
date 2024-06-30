from pydantic import BaseModel
from typing import List
from .field_response_schema import FieldResponseSchema

class ListFieldsByUserResponseSchema(BaseModel):
    """ Define como uma listagem de trilhas de estudos será retornada.
    """
    fields:List[FieldResponseSchema]