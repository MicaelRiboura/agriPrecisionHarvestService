from modules.shared.config.db_sqlite import Session
from modules.harvest_history.daos.harvest_history.harvest_history_dao_alchemy import HarvestHistoryDAO

def delete_harvest(query):
    try:
        session = Session()
        
        harvest_history_dao = HarvestHistoryDAO()

        response = harvest_history_dao.delete(session, query.id, query.user)

        if not response:
            error_msg = "Colheita não encontrada!"
            return {"message": error_msg}, 404

        success_msg = "Colheita removida com sucesso!"
        return {"message": success_msg}, 200
            
    except Exception as e:
        print('error: ', e)
        error_msg = "Não foi possível deletar o registro de colheita!"

        return {"message": error_msg}, 404