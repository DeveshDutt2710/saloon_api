from utility.pagination_utilities import PaginationUtilities
from .enquiry_manager import EnquiryManager
from .serializers import EnquirySerializer
from ..serializers import BsonSerializer
from ..models import Enquiries
from djongo.models.fields import ObjectId
from djongo.models import Q


class EnquiryImpl(EnquiryManager):

    enquiry_id = None
    page = 1
    page_size = 10

    def __init__(self, enquiry_id: str = None, page: int = 1, page_size: int = 10):
        self.set_enquiry_id(enquiry_id)
        self.page = page
        self.page_size = page_size

    def set_enquiry_id(self, enquiry_id):
        self.enquiry_id = enquiry_id

    def get_enquiry_id(self):
        return self.enquiry_id

    def fetch_all_enquiries(self) -> dict:
        enquiries = Enquiries.objects.all()  # .filter(is_deleted=False)

        enquiries = PaginationUtilities.paginate_results(enquiries,
                                                         page_number=self.page,
                                                         page_size=self.page_size)

        enquiries_data = EnquirySerializer(enquiries, many=True)

        response = {
            'success': True,
            'enquiries': enquiries_data.data
        }

        return response

    def fetch_enquiry_by_id(self) -> dict:
        enquiry = Enquiries.get_object_or_raise_exception(self.get_enquiry_id())

        enquiry_data = EnquirySerializer(enquiry)

        response = {
            'success': True,
            'enquiry': enquiry_data.data
        }

        return response

    def create_enquiry(self, data) -> dict:

        Enquiries(**data).save()

        response = {
            'success': True,
        }

        return response

    def update_enquiry(self, data) -> dict:

        Enquiries.objects.filter(pk=ObjectId(self.get_enquiry_id())).update(**data)

        response = {
            'success': True,
        }

        return response

    def delete_enquiry(self) -> dict:
        enquiry = Enquiries.get_object_or_raise_exception(self.get_enquiry_id())

        enquiry.delete_enquiry()

        response = {
            'success': True,
        }

        return response

    def search_enquiry(self, query):

        enquiries = [i for i in Enquiries.objects.mongo_find(
            {'$or': [{'email': {"$regex": f'.*{query}.*', "$options": "i"}},
                     {'phone': {"$regex": f'.*{query}.*', "$options": "i"}}
                     ]
             }
        )]

        enquiries = PaginationUtilities.paginate_results(enquiries,
                                                         page_number=self.page,
                                                         page_size=self.page_size)

        data = BsonSerializer.serialize_search_results(enquiries)

        response = {
            'success': True,
            'enquiries': data
        }

        return response
