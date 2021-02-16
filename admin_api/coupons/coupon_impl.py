from utility.pagination_utilities import PaginationUtilities
from .coupon_manager import CouponManager
from .serializers import CouponSerializer
from ..serializers import BsonSerializer
from ..models import Coupons
from djongo.models.fields import ObjectId
from djongo.models import Q


class CouponImpl(CouponManager):

    coupon_id = None
    page = 1
    page_size = 10

    def __init__(self, coupon_id: str = None, page: int = 1, page_size: int = 10):
        self.set_coupon_id(coupon_id)
        self.page = page
        self.page_size = page_size

    def set_coupon_id(self, coupon_id):
        self.coupon_id = coupon_id

    def get_coupon_id(self):
        return self.coupon_id

    def fetch_all_coupons(self) -> dict:
        coupons = Coupons.objects.all()  # .filter(is_deleted=False)

        coupons = PaginationUtilities.paginate_results(coupons,
                                                       page_number=self.page,
                                                       page_size=self.page_size)

        coupon_data = CouponSerializer(coupons, many=True)

        response = {
            'success': True,
            'coupons': coupon_data.data
        }

        return response

    def fetch_coupon_by_id(self) -> dict:
        coupons = Coupons.get_object_or_raise_exception(self.get_coupon_id())

        coupon_data = CouponSerializer(coupons)

        response = {
            'success': True,
            'coupon': coupon_data.data
        }

        return response

    def create_coupon(self, data) -> dict:

        Coupons(**data).save()

        response = {
            'success': True,
        }

        return response

    def update_coupon(self, data) -> dict:

        Coupons.objects.filter(pk=ObjectId(self.get_coupon_id())).update(**data)

        response = {
            'success': True,
        }

        return response

    def delete_coupon(self) -> dict:
        coupon = Coupons.get_object_or_raise_exception(self.get_coupon_id())

        coupon.delete_coupon()

        response = {
            'success': True,
        }

        return response

    def search_coupon(self, query):

        coupons = [i for i in Coupons.objects.mongo_find(
            {'$or': [{'name': {"$regex": f'.*{query}.*', "$options": "i"}},
                     ]
             }
        )]

        coupons = PaginationUtilities.paginate_results(coupons,
                                                       page_number=self.page,
                                                       page_size=self.page_size)

        data = BsonSerializer.serialize_search_results(coupons)

        response = {
            'success': True,
            'coupons': data
        }

        return response
