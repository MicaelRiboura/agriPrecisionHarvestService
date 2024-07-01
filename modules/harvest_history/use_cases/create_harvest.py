from modules.shared.config.db_sqlite import Session
from modules.harvest_history.daos.harvest_history.harvest_history_dao_alchemy import HarvestHistoryDAO

def create_harvest(form):
    try:
        session = Session()
        harvest_history_dao = HarvestHistoryDAO()

        field = harvest_history_dao.create(session, form)
        
        return field, 200

    except Exception as e:
        # caso um erro fora do previsto
        print('error: ', e)
        error_msg = "Não foi possível salvar a nova colheita!"
        return {"message": error_msg}, 400
