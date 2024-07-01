from pydantic import BaseModel

class DeleteResponseSchema(BaseModel):
    """ Define como uma mensagem de registro removido com sucesso é representada.
    """
    message: str
