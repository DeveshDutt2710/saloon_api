import abc


class OrderManager(metaclass=abc.ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        return ((hasattr(subclass, 'fetch_all_orders') and callable(subclass.fetch_all_orders)) and
                (hasattr(subclass, 'fetch_order_by_id') and callable(subclass.fetch_order_by_id)) and
                (hasattr(subclass, 'create_order') and callable(subclass.create_order)) and
                (hasattr(subclass, 'update_order') and callable(subclass.update_order)) and
                (hasattr(subclass, 'search_order') and callable(subclass.search_order)) and
                (hasattr(subclass, 'delete_order') and callable(subclass.delete_order)) or
                NotImplemented)

    @abc.abstractmethod
    def fetch_all_orders(self) -> dict:
        """
        fetch all orders
        """
        raise NotImplementedError

    @abc.abstractmethod
    def fetch_order_by_id(self) -> dict:
        """
        get order by id
        """
        raise NotImplementedError

    @abc.abstractmethod
    def create_order(self, data) -> dict:
        """
        create new order
        """
        raise NotImplementedError

    @abc.abstractmethod
    def update_order(self, data) -> dict:
        """
        update existing order
        """
        raise NotImplementedError

    @abc.abstractmethod
    def delete_order(self) -> dict:
        """
        delete order
        """
        raise NotImplementedError

    @abc.abstractmethod
    def search_order(self, query) -> dict:
        """
        search order by name, email or phone
        """
        raise NotImplementedError
