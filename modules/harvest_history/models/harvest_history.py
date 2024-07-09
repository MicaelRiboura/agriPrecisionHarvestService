from sqlalchemy import Column, String, Integer, Float, ForeignKey, Date
from modules.shared.config.model.base import Base
from modules.shared.config.model.serializer import Serializer
from datetime import datetime

class HarvestHistory(Base):
    __tablename__ = 'harvest_history'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    total_production = Column(Integer)
    field = Column(Integer, ForeignKey('field.id'), nullable=False)
    user = Column(String(500))

    def __init__(self, date: str, total_production: float, field: int, user: str):
        self.date = datetime.strptime(date, '%Y-%m-%d')
        self.total_production = total_production
        self.field = field
        self.user = user

    def serialize(self):
        harvest_history = Serializer.serialize(self)
        harvest_history['date'] = datetime.strftime(self.date, '%Y-%m-%d')
        return harvest_history