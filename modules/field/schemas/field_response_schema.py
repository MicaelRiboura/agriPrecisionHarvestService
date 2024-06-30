from pydantic import BaseModel
from typing import Optional, List

class FieldResponseSchema(BaseModel):
    """ Define como um talhão deve ser representado
    """
    id:int = 1
    area:float = 20.0
    user: str
    # items:Optional[List[ItemResponseSchema]]