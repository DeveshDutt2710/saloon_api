import abc


class CouponManager(metaclass=abc.ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        return ((hasattr(subclass, 'fetch_all_coupons') and callable(subclass.fetch_all_coupons)) and
                (hasattr(subclass, 'fetch_coupon_by_id') and callable(subclass.fetch_coupon_by_id)) and
                (hasattr(subclass, 'create_coupon') and callable(subclass.create_coupon)) and
                (hasattr(subclass, 'update_coupon') and callable(subclass.update_coupon)) and
                (hasattr(subclass, 'delete_coupon') and callable(subclass.delete_coupon)) or
                NotImplemented)

    @abc.abstractmethod
    def fetch_all_coupons(self) -> dict:
        """
        fetch all coupons
        """
        raise NotImplementedError

    @abc.abstractmethod
    def fetch_coupon_by_id(self) -> dict:
        """
        get coupons by id
        """
        raise NotImplementedError

    @abc.abstractmethod
    def create_coupon(self, data) -> dict:
        """
        create a new coupons
        """
        raise NotImplementedError

    @abc.abstractmethod
    def update_coupon(self, data) -> dict:
        """
        update a existing coupons
        """
        raise NotImplementedError

    @abc.abstractmethod
    def delete_coupon(self) -> dict:
        """
        delete coupon
        """
        raise NotImplementedError

    @abc.abstractmethod
    def search_coupon(self, query) -> dict:
        """
        search coupons by name
        """
        raise NotImplementedError
