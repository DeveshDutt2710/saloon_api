import abc


class EnquiryManager(metaclass=abc.ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        return ((hasattr(subclass, 'fetch_all_enquiries') and callable(subclass.fetch_all_enquiries)) and
                (hasattr(subclass, 'fetch_enquiry_by_id') and callable(subclass.fetch_enquiry_by_id)) and
                (hasattr(subclass, 'create_enquiry') and callable(subclass.create_enquiry)) and
                (hasattr(subclass, 'update_enquiry') and callable(subclass.update_enquiry)) and
                (hasattr(subclass, 'search_enquiry') and callable(subclass.search_enquiry)) and
                (hasattr(subclass, 'delete_enquiry') and callable(subclass.delete_enquiry)) or
                NotImplemented)

    @abc.abstractmethod
    def fetch_all_enquiries(self) -> dict:
        """
        fetch all enquiries
        """
        raise NotImplementedError

    @abc.abstractmethod
    def fetch_enquiry_by_id(self) -> dict:
        """
        get enquiry by id
        """
        raise NotImplementedError

    @abc.abstractmethod
    def create_enquiry(self, data) -> dict:
        """
        create new enquiry
        """
        raise NotImplementedError

    @abc.abstractmethod
    def update_enquiry(self, data) -> dict:
        """
        update existing enquiry
        """
        raise NotImplementedError

    @abc.abstractmethod
    def delete_enquiry(self) -> dict:
        """
        delete enquiry
        """
        raise NotImplementedError

    @abc.abstractmethod
    def search_enquiry(self, query) -> dict:
        """
        search enquiry
        """
        raise NotImplementedError
