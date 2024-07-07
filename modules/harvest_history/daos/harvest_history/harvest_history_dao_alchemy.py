from modules.harvest_history.models import HarvestHistory
from sqlalchemy import func
from .abstract_harvest_history_dao import AbstractHarvestHistoryDAO
from modules.field.models import Field

class HarvestHistoryDAO(AbstractHarvestHistoryDAO):
    def find_by_user_and_field(self, session, user, field):
        harvest_history = session.query(HarvestHistory).filter(HarvestHistory.user == user)\
            .filter(HarvestHistory.field == field)
        
        harvest_history_serialized = []
        if harvest_history:
            for harvest in harvest_history:
                harvest_history_serialized.append(harvest.serialize())
        
        return harvest_history_serialized
    
    def show_productivity_map(self, session, user):

        results = session.query(
            Field.id,
            func.avg(HarvestHistory.total_production).label('total_production'),
        ).join(HarvestHistory).group_by(Field.id).all()

        response = []

        for field_id, average in results:
            response.append({ 'field': field_id, 'average': average })

        return response

    def create(self, session, form):
        harvest = HarvestHistory(
            date=form.date,
            total_production=form.total_production,
            field=form.field,
            user=form.user,
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