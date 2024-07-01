from pydantic import BaseModel
from typing import List
from .harvest_response_schema import HarvestResponseSchema

class ListHarvestHistoryByUserAndFieldResponseSchema(BaseModel):
    """ Define como uma listagem de histórico de colheitas será retornada.
    """
    history:List[HarvestResponseSchema]