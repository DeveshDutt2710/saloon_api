import abc


class MasterProductManager(metaclass=abc.ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        return ((hasattr(subclass, 'fetch_all_master_products') and callable(subclass.fetch_all_master_products)) and
                (hasattr(subclass, 'fetch_master_product_by_id') and callable(subclass.fetch_master_product_by_id)) and
                (hasattr(subclass, 'create_master_product') and callable(subclass.create_master_product)) and
                (hasattr(subclass, 'update_master_product') and callable(subclass.update_master_product)) and
                (hasattr(subclass, 'search_master_product') and callable(subclass.search_master_product)) and
                (hasattr(subclass, 'delete_master_product') and callable(subclass.delete_master_product)) or
                NotImplemented)

    @abc.abstractmethod
    def fetch_all_master_products(self) -> dict:
        """
        fetch all master products
        """
        raise NotImplementedError

    @abc.abstractmethod
    def fetch_master_product_by_id(self) -> dict:
        """
        get master product from id
        """
        raise NotImplementedError

    @abc.abstractmethod
    def create_master_product(self, data) -> dict:
        """
        create master product
        """
        raise NotImplementedError

    @abc.abstractmethod
    def update_master_product(self, data) -> dict:
        """
        update existing master product
        """
        raise NotImplementedError

    @abc.abstractmethod
    def delete_master_product(self) -> dict:
        """
        delete master product
        """
        raise NotImplementedError

    @abc.abstractmethod
    def search_master_product(self, query) -> dict:
        """
        search master product by name
        """
        raise NotImplementedError
