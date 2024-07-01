from modules.harvest_history.models import HarvestHistory
from .abstract_harvest_history import AbstractHarvestHistoryDAO

class HarvestHistoryDAO(AbstractHarvestHistoryDAO):
    def find_by_user_and_field(self, session, user, field):
        harvest_history = session.query(HarvestHistory).filter(HarvestHistory.user == user)\
            .filter(HarvestHistory.field == field)
        
        harvest_history_serialized = []
        if harvest_history:
            for field in harvest_history:
                harvest_history_serialized.append(field.serialize())
        
        return harvest_history_serialized

    def create(self, session, form):
        harvest = HarvestHistory(
            area=form.date,
            user=form.total_production,
        )
    
        session.add(harvest)
        session.commit()

        return harvest.serialize()
    
    def delete(self, session, id, user):
        count = session.query(HarvestHistory).filter(HarvestHistory.user == user).filter(HarvestHistory.id == id).delete()
        session.commit()
        
        if not count:
            return False
        
        return True