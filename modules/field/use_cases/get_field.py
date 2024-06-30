from modules.shared.config.db_sqlite import Session
from modules.field.daos.field.field_dao_alchemy import FieldDAO

def get_field(query):
    try:
        session = Session()
        field_dao = FieldDAO()

        if not query.user:
            error_msg = "Usuário não encontrado!"
            return {"message": error_msg}, 404
        
        if not query.id:
            error_msg = "Talhão não encontrado!"
            return {"message": error_msg}, 404

        field_response = field_dao.find_by_id_and_user(session, query.id, query.user)

        return { 'field': field_response }, 200
        
    except Exception as e:
        print('error: ', e)
        error_msg = "Não foi possível retornar o talhão!"

        return {"message": error_msg}, 404