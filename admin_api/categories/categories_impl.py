from utility.pagination_utilities import PaginationUtilities
from .categories_manager import CategoriesManager
from .serializers import CategorySerializer
from ..serializers import BsonSerializer
from ..models import Categories
from djongo.models.fields import ObjectId


class CategoryImpl(CategoriesManager):
    category_id = None
    page = 1
    page_size = 10

    def __init__(self, category_id: str = None, page: int = 1, page_size: int = 10):
        self.set_category_id(category_id)
        self.page = page
        self.page_size = page_size

    def set_category_id(self, category_id):
        self.category_id = category_id

    def get_category_id(self):
        return self.category_id

    def fetch_all_categories(self) -> dict:
        categories = Categories.objects.all()  # .filter(is_deleted=False)

        categories = PaginationUtilities.paginate_results(categories,
                                                          page_number=self.page,
                                                          page_size=self.page_size)

        category_data = CategorySerializer(categories, many=True)

        response = {
            'success': True,
            'categories': category_data.data
        }

        return response

    def fetch_category_by_id(self) -> dict:
        categorys = Categories.get_object_or_raise_exception(self.get_category_id())

        category_data = CategorySerializer(categorys)

        response = {
            'success': True,
            'category': category_data.data
        }

        return response

    def create_category(self, data) -> dict:
        Categories(**data).save()

        response = {
            'success': True,
        }

        return response

    def update_category(self, data) -> dict:
        Categories.objects.filter(pk=ObjectId(self.get_category_id())).update(**data)

        response = {
            'success': True,
        }

        return response

    def delete_category(self) -> dict:
        category = Categories.get_object_or_raise_exception(self.get_category_id())

        category.delete_category()

        response = {
            'success': True,
        }

        return response

    def search_category(self, query):
        categories = [i for i in Categories.objects.mongo_find(
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

        categories = PaginationUtilities.paginate_results(categories,
                                                          page_number=self.page,
                                                          page_size=self.page_size)

        data = BsonSerializer.serialize_search_results(categories)

        response = {
            'success': True,
            'categories': data
        }

        return response
