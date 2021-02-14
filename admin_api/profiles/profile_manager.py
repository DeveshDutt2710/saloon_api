import abc

class ProfileManager(metaclass=abc.ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        return ((hasattr(subclass, 'create_profile') and callable(subclass.create_profile)) and
                (hasattr(subclass, 'update_profile') and callable(subclass.update_profile)) and
                (hasattr(subclass, 'delete_profile') and callable(subclass.delete_profile)) or
                NotImplemented)

    @abc.abstractmethod
    def fetch_all_profiles(self) -> dict:
        """
        fetching all profile
        """
        raise NotImplementedError
    
    @abc.abstractmethod
    def create_profile(self, data) -> dict:
        """
        create new profile
        """
        raise NotImplementedError

    @abc.abstractmethod
    def update_profile(self, data) -> dict:
        """
        update existing profile
        """
        raise NotImplementedError

    @abc.abstractmethod
    def delete_profile(self) -> dict:
        """
        delete existing profile
        """
        raise NotImplementedError