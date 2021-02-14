from utility.pagination_utilities import PaginationUtilities
from .profile_manager import ProfileManager
from .serializers import ProfileSerializer
from ..serializers import BsonSerializer
from ..models import Profiles
from djongo.models.fields import ObjectId


class ProfileImpl(ProfileManager):
    profile_id=None
    page=1
    page_size=10

    def __init__(self,profile_id:str=None, page:int =1,page_size:int =10):
        self.set_profile_id(profile_id)
        self.page=page
        self.page_size=page_size

    def set_profile_id(self, profile_id):
        self.profile_id=profile_id

    def get_profile_id(self):
        return self.profile_id
    
    def fetch_all_profiles(self) -> dict:
        profiles = Profiles.objects.all()  # .filter(is_deleted=False)

        profiles = PaginationUtilities.paginate_results(profiles,
                                                        page_number=self.page,
                                                        page_size=self.page_size)

        profile_data = ProfileSerializer(profiles, many=True)

        response = {
            'success': True,
            'profiles': profile_data.data
        }

        return response

    def create_profile(self,data)->dict:
        Profiles(**data).save()

        response={
            'success':True,
        }

        return response

    def update_profile(self, data) -> dict:

        Profiles.objects.filter(pk=ObjectId(self.get_profile_id())).update(**data)

        response = {
            'success': True,
        }

        return response

    def delete_profile(self) -> dict:
        profile = Profiles.get_object_or_raise_exception(self.get_profile_id())

        profile.delete_profile()

        response = {
            'success': True,
        }

        return response