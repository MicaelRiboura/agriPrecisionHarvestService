from modules.shared.config.db_sqlite import Session
from modules.harvest_history.daos.harvest_history.harvest_history_dao_alchemy import HarvestHistoryDAO

def map_productivity_fields(query):
    try:
        session = Session()
        harvest_history_dao = HarvestHistoryDAO()


        if not query.user:
            error_msg = "Usuário não encontrado!"
            return {"message": error_msg}, 404

        fields_response = harvest_history_dao.show_productivity_map(session, query.user)

        return { 'fields': fields_response }, 200
        
    except Exception as e:
        print('error: ', e)
        error_msg = "Não foi possível listar os talhões!"

        return {"message": error_msg}, 404