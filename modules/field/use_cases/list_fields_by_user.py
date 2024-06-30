from modules.shared.config.db_sqlite import Session
from modules.field.daos.field.field_dao_alchemy import FieldDAO

def list_fields_by_user(query):
    try:
        session = Session()
        field_dao = FieldDAO()


        if not query.user:
            error_msg = "Usuário não encontrado!"
            return {"message": error_msg}, 404

        fields_response = field_dao.find_by_user(session, query.user)

        return { 'fields': fields_response }, 200
        
    except Exception as e:
        print('error: ', e)
        error_msg = "Não foi possível listar os talhões!"

        return {"message": error_msg}, 404