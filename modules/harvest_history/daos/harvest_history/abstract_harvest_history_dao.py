from abc import ABC, abstractmethod


class AbstractHarvestHistoryDAO(ABC):
    @abstractmethod
    def create(self, session, form):
        raise NotImplementedError

    @abstractmethod
    def find_by_user_and_field(self, session, user, field):
        raise NotImplementedError
    
    @abstractmethod
    def delete(self, session, id):
        raise NotImplementedError
    
    @abstractmethod
    def show_productivity_map(self, session, user):
        raise NotImplementedError