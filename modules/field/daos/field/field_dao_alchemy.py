from modules.field.models import Field
from .abstract_field_dao import AbstractFieldDAO

class FieldDAO(AbstractFieldDAO):
    def find_by_user(self, session, user):
        fields = session.query(Field).filter(Field.user == user)
        fields_serialized = []
        if fields:
            for field in fields:
                fields_serialized.append(field.serialize())
        
        return fields_serialized
    
    def find_by_id_and_user(self, session, id, user):
        field = session.query(Field).filter(Field.user == user).filter(Field.id == id).first()
        return field.serialize()

    def create(self, session, form):
        field = Field(
            area=form.area,
            planting=form.planting,
            user=form.user,
        )
    
        session.add(field)
        session.commit()

        return field.serialize()
    

    def edit(self, session, form):
        field = session.query(Field).filter(Field.user == form.user).filter(Field.id == form.id).first()
        field.area = form.area
        field.planting = form.planting
        session.commit()

        return field.serialize()
    
    def delete(self, session, id, user):
        count = session.query(Field).filter(Field.user == user).filter(Field.id == id).delete()
        session.commit()
        
        if not count:
            return False
        
        return True