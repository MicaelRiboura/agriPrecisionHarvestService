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
    
    def find_by_id(self, session, id):
       raise NotImplementedError
    

    def create(self, session, form, user):
        raise NotImplementedError
    

    def edit(self, session, form, user):
        raise NotImplementedError
    
    def delete(self, session, form, user):
        raise NotImplementedError