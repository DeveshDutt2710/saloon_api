from utility.pagination_utilities import PaginationUtilities
from .master_product_manager import MasterProductManager
from .serializers import MasterProductSerializer
from ..serializers import BsonSerializer
from ..models import MasterProduct
from djongo.models.fields import ObjectId


class MasterProductImpl(MasterProductManager):
    master_product_id = None
    page = 1
    page_size = 10

    def __init__(self, master_product_id: str = None, page: int = 1, page_size: int = 10):
        self.set_master_product_id(master_product_id)
        self.page = page
        self.page_size = page_size

    def set_master_product_id(self, master_product_id):
        self.master_product_id = master_product_id

    def get_master_product_id(self):
        return self.master_product_id

    def fetch_all_master_products(self) -> dict:
        master_products = MasterProduct.objects.all()  # .filter(is_deleted=False)

        master_products = PaginationUtilities.paginate_results(master_products,
                                                               page_number=self.page,
                                                               page_size=self.page_size)

        master_product_data = MasterProductSerializer(master_products, many=True)

        response = {
            'success': True,
            'master_products': master_product_data.data
        }

        return response

    def fetch_master_product_by_id(self) -> dict:
        master_products = MasterProduct.get_object_or_raise_exception(self.get_master_product_id())

        master_product_data = MasterProductSerializer(master_products)

        response = {
            'success': True,
            'master_product': master_product_data.data
        }

        return response

    def create_master_product(self, data) -> dict:
        MasterProduct(**data).save()

        response = {
            'success': True,
        }

        return response

    def update_master_product(self, data) -> dict:
        MasterProduct.objects.filter(pk=ObjectId(self.get_master_product_id())).update(**data)

        response = {
            'success': True,
        }

        return response

    def delete_master_product(self) -> dict:
        master_product = MasterProduct.get_object_or_raise_exception(self.get_master_product_id())

        master_product.delete_master_product()

        response = {
            'success': True,
        }

        return response

    def search_master_product(self, query):
        master_products = [i for i in MasterProduct.objects.mongo_find(
            {
                '$or': [
                    {'name':
                        {
                            "$regex": f'.*{query}.*',
                            "$options": "i"
                        }
                    }
                ]
            }
        )]

        master_products = PaginationUtilities.paginate_results(master_products,
                                                               page_number=self.page,
                                                               page_size=self.page_size)

        data = BsonSerializer.serialize_search_results(master_products)

        response = {
            'success': True,
            'master_products': data
        }

        return response
