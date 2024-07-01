from modules.shared.config.db_sqlite import Session
from modules.harvest_history.daos.harvest_history.harvest_history_dao_alchemy import HarvestHistoryDAO

def list_harvest_history_by_user_and_field(query):
    try:
        session = Session()
        harvest_history_dao = HarvestHistoryDAO()


        if not query.user:
            error_msg = "Usuário não encontrado!"
            return {"message": error_msg}, 404
        
        if not query.field:
            error_msg = "Talhão não encontrado!"
            return {"message": error_msg}, 404

        harvest_history_response = harvest_history_dao.find_by_user_and_field(session, query.user, query.field)

        return { 'history': harvest_history_response }, 200
        
    except Exception as e:
        print('error: ', e)
        error_msg = "Não foi possível listar o histórico de colheitas!"

        return {"message": error_msg}, 404