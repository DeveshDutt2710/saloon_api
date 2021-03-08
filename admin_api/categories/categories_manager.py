import abc


class CategoriesManager(metaclass=abc.ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        return ((hasattr(subclass, 'fetch_all_categories') and callable(subclass.fetch_all_categories)) and
                (hasattr(subclass, 'fetch_category_by_id') and callable(subclass.fetch_category_by_id)) and
                (hasattr(subclass, 'create_category') and callable(subclass.create_category)) and
                (hasattr(subclass, 'update_category') and callable(subclass.update_category)) and
                (hasattr(subclass, 'search_category') and callable(subclass.search_category)) and
                (hasattr(subclass, 'delete_category') and callable(subclass.delete_category)) or
                NotImplemented)

    @abc.abstractmethod
    def fetch_all_categories(self) -> dict:
        """
        fetch all master products
        """
        raise NotImplementedError

    @abc.abstractmethod
    def fetch_category_by_id(self) -> dict:
        """
        get master product from id
        """
        raise NotImplementedError

    @abc.abstractmethod
    def create_category(self, data) -> dict:
        """
        create master product
        """
        raise NotImplementedError

    @abc.abstractmethod
    def update_category(self, data) -> dict:
        """
        update existing master product
        """
        raise NotImplementedError

    @abc.abstractmethod
    def delete_category(self) -> dict:
        """
        delete master product
        """
        raise NotImplementedError

    @abc.abstractmethod
    def search_category(self, query) -> dict:
        """
        search master product by name
        """
        raise NotImplementedError
