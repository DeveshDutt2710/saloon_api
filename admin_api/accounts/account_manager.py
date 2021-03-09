import abc


class AccountManager(metaclass=abc.ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        return ((hasattr(subclass, 'fetch_all_accounts') and callable(subclass.fetch_all_accounts)) and
                (hasattr(subclass, 'fetch_account_by_id') and callable(subclass.fetch_account_by_id)) and
                (hasattr(subclass, 'create_account') and callable(subclass.create_account)) and
                (hasattr(subclass, 'update_account') and callable(subclass.update_account)) and
                (hasattr(subclass, 'search_account') and callable(subclass.search_account)) and
                (hasattr(subclass, 'delete_account') and callable(subclass.delete_account)) or
                NotImplemented)

    @abc.abstractmethod
    def fetch_all_accounts(self) -> dict:
        """
        fetching the chatroom from chatroom id
        """
        raise NotImplementedError

    @abc.abstractmethod
    def fetch_account_by_id(self) -> dict:
        """
        fetching the chatroom from chatroom id
        """
        raise NotImplementedError

    @abc.abstractmethod
    def create_account(self, data) -> dict:
        """
        fetching the chatroom from chatroom id
        """
        raise NotImplementedError

    @abc.abstractmethod
    def update_account(self, data) -> dict:
        """
        fetching the chatroom from chatroom id
        """
        raise NotImplementedError

    @abc.abstractmethod
    def delete_account(self) -> dict:
        """
        fetching the chatroom from chatroom id
        """
        raise NotImplementedError

    @abc.abstractmethod
    def search_account(self, query) -> dict:
        """
        fetching the chatroom from chatroom id
        """
        raise NotImplementedError
