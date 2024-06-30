from pydantic import BaseModel
from typing import Optional, List

class FieldByIdQuerySchema(BaseModel):
    """ Define como um talhão deve ser representado
    """
    id:int = 1
    user: str = ""