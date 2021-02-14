from djongo import models
from .model_choices import *
from utility.exception_utilities import *
from utility.time_utilities import TimeUtilities
from djongo.models.fields import ObjectId
from datetime import datetime

class Profiles(models.Model):
    objects = models.DjongoManager()

    _id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=255, null=False)
    #accountId = models.OneToOneField(Account, on_delete=models.CASCADE)
    profileType = models.CharField(choices=COUPON_TYPE, max_length=1024, default=COUPON_TYPE_FLAT)

    vendorDescription = models.TextField(null=True)
    contact = models.JSONField()

    address = models.JSONField()

    privacySetting = models.JSONField()

    dob = models.DateTimeField()

    gender = models.CharField(max_length=10)
    image = models.TextField()

    lastAppActivity = models.DateTimeField(null=True)

    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()

    is_deleted = models.BooleanField(default=False)
    is_admin_verified = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'profiles'

    @staticmethod
    def get_object_or_raise_exception(profile_id):
        try:
            return Profiles.objects.get(pk=ObjectId(profile_id))
        except Profiles.DoesNotExist:
            response = {
                'success': False,
                'detail': f'Profile with id {profile_id} does not exist'
            }
            raise InvalidProfileException(response, status_code=status_codes.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get_object_or_none(profile_id):
        try:
            return Profiles.objects.get(pk=ObjectId(profile_id))
        except Profiles.DoesNotExist:
            return None

    def save(self, *args, **kwargs):

        current_time = datetime.now()

        if not self.createdAt:
            self.createdAt = current_time

        self.updatedAt = current_time

        super(Profiles, self).save(*args, **kwargs)
