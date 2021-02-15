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

    def delete_profile(self):
        self.is_deleted = True
        self.save()

    def save(self, *args, **kwargs):

        current_time = datetime.now()

        if not self.createdAt:
            self.createdAt = current_time

        self.updatedAt = current_time

        super(Profiles, self).save(*args, **kwargs)


class Products(models.Model):
    objects = models.DjongoManager()

    _id = models.ObjectIdField()
    name = models.TextField()
    description = models.TextField()
    price = models.IntegerField()

    sales = models.IntegerField(default=0)
    timings = models.JSONField()
    productAvailability = models.BooleanField(default=False)
    rating = models.IntegerField(default=5)

    productType = models.CharField(choices=PRODUCT_TYPES, max_length=1024, default=PRODUCT_TYPE_PRODUCT)
    vendorId = models.ForeignKey(Profiles, on_delete=models.CASCADE)

    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()

    is_deleted = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'products'

    @staticmethod
    def get_object_or_raise_exception(product_id):
        try:
            return Products.objects.get(pk=ObjectId(product_id))
        except Products.DoesNotExist:
            response = {
                'success': False,
                'detail': f'Product with id {product_id} does not exist'
            }
            raise InvalidProfileException(response, status_code=status_codes.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get_object_or_none(product_id):
        try:
            return Products.objects.get(pk=ObjectId(product_id))
        except Products.DoesNotExist:
            return None

    def delete_product(self):
        self.is_deleted = True
        self.save()

    def save(self, *args, **kwargs):

        current_time = datetime.now()

        if not self.createdAt:
            self.createdAt = current_time

        self.updatedAt = current_time

        super(Products, self).save(*args, **kwargs)

class Enquiries(models.Model):
    objects = models.DjongoManager()

    _id = models.ObjectIdField()
    profileId = models.TextField()
    productId = models.TextField()
    dateCreated = models.DateTimeField(auto_now_add=True)

    status = models.CharField(choices=ENQUIRY_STATUS, max_length=1024, default=ENQUIRY_STATUS_PENDING)

    quantity = models.IntegerField(default=1)

    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()

    is_deleted = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'enquiries'

    @staticmethod
    def get_object_or_raise_exception(enquiry_id):
        try:
            return Enquiries.objects.get(pk=ObjectId(enquiry_id))
        except Enquiries.DoesNotExist:
            response = {
                'success': False,
                'detail': f'Enquiry with id {enquiry_id} does not exist'
            }
            raise InvalidProfileException(response, status_code=status_codes.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get_object_or_none(enquiry_id):
        try:
            return Enquiries.objects.get(pk=ObjectId(enquiry_id))
        except Enquiries.DoesNotExist:
            return None

    def delete_enquiry(self):
        self.is_deleted = True
        self.save()

    def save(self, *args, **kwargs):

        current_time = datetime.now()

        if not self.createdAt:
            self.createdAt = current_time

        self.updatedAt = current_time

        super(Enquiries, self).save(*args, **kwargs)