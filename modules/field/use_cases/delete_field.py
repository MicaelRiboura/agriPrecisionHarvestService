from modules.shared.config.db_sqlite import Session
from modules.field.daos.field.field_dao_alchemy import FieldDAO

def delete_field(query):
    try:
        session = Session()
        
        field_dao = FieldDAO()

        response = field_dao.delete(session, query.id, query.user)

        if not response:
            error_msg = "Talhão não encontrado!"
            return {"message": error_msg}, 404

        success_msg = "Talhão removido com sucesso!"
        return {"message": success_msg}, 200
            
    except Exception as e:
        print('error: ', e)
        error_msg = "Não foi possível deletar o talhão!"

        return {"message": error_msg}, 404