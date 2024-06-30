from pydantic import BaseModel

class DeleteFieldSchema(BaseModel):
    """ Define como uma mensagem de talhão removido com sucesso é representada.
    """
    message: str