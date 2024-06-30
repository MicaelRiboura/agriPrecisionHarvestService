from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from modules.shared.config.model.base import Base
from modules.shared.config.model.serializer import Serializer
from modules.harvest_history.models.harvest_history import HarvestHistory

class Field(Base):
    __tablename__ = 'field'

    id = Column(Integer, primary_key=True)
    area = Column(Float)
    planting = Column(String(500))
    user = Column(String(500))
    history = relationship('HarvestHistory')

    def __init__(self, area: float, planting: str, user: str):
        self.area = area
        self.planting = planting
        self.user = user


    def add_history(self, history: HarvestHistory):
        self.history.append(history)

    def serialize(self):
        field = Serializer.serialize(self)
        field['history'] = Serializer.serialize_list(field['history'])

        return field