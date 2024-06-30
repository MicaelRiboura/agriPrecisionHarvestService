from sqlalchemy import Column, String, Integer, Float, ForeignKey, Date
from modules.shared.config.model.base import Base
from modules.shared.config.model.serializer import Serializer

class HarvestHistory(Base):
    __tablename__ = 'harvest_history'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    humidity = Column(Float)
    total_production = Column(Integer)
    field = Column(Integer, ForeignKey('field.id'), nullable=False)
    user = Column(String(500))

    def __init__(self, date: str, humidity: float, total_production: float):
        self.date = date
        self.humidity = humidity
        self.total_production = total_production

    def serialize(self):
        harvest_history = Serializer.serialize(self)
        return harvest_history