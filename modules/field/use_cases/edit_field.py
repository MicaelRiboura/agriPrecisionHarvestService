from modules.shared.config.db_sqlite import Session
from modules.field.daos.field.field_dao_alchemy import FieldDAO

def edit_field(form):
    try:
        session = Session()
        field_dao = FieldDAO()

        field = field_dao.edit(session, form)
        
        return field, 200

    except Exception as e:
        # caso um erro fora do previsto
        print('error: ', e)
        error_msg = "Não foi possível salvar o talhão!"
        return {"message": error_msg}, 400
