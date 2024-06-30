from abc import ABC, abstractmethod


class AbstractFieldDAO(ABC):
    @abstractmethod
    def create(self, session, form, user):
        raise NotImplementedError

    @abstractmethod
    def find_by_user(self, session, user):
        raise NotImplementedError
    
    @abstractmethod
    def find_by_id(self, session, id):
        raise NotImplementedError

    @abstractmethod
    def edit(self, session, id):
        raise NotImplementedError
    
    @abstractmethod
    def delete(self, session, id):
        raise NotImplementedError
    