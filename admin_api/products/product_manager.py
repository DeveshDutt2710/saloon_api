import abc


class ProductManager(metaclass=abc.ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        return ((hasattr(subclass, 'fetch_all_products') and callable(subclass.fetch_all_products)) and
                (hasattr(subclass, 'fetch_product_by_id') and callable(subclass.fetch_product_by_id)) and
                (hasattr(subclass, 'create_product') and callable(subclass.create_product)) and
                (hasattr(subclass, 'update_product') and callable(subclass.update_product)) and
                (hasattr(subclass, 'search_product') and callable(subclass.search_product)) and
                (hasattr(subclass, 'delete_product') and callable(subclass.delete_product)) or
                NotImplemented)

    @abc.abstractmethod
    def fetch_all_products(self) -> dict:
        """
        fetch all products
        """
        raise NotImplementedError

    @abc.abstractmethod
    def fetch_product_by_id(self) -> dict:
        """
        get product by id
        """
        raise NotImplementedError

    @abc.abstractmethod
    def create_product(self, data) -> dict:
        """
        create new product
        """
        raise NotImplementedError

    @abc.abstractmethod
    def update_product(self, data) -> dict:
        """
        update existing product
        """
        raise NotImplementedError

    @abc.abstractmethod
    def delete_product(self) -> dict:
        """
        delete product
        """
        raise NotImplementedError

    @abc.abstractmethod
    def search_product(self, query) -> dict:
        """
        search product by name
        """
        raise NotImplementedError
