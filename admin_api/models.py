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

class Orders(models.Model):
    objects = models.DjongoManager()

    _id = models.ObjectIdField()

    productId = models.TextField()
    vendorId = models.TextField()
    customerId = models.TextField()
    customerName = models.TextField()

    contact = models.JSONField()

    payment = models.JSONField()

    time = models.JSONField()

    date = models.DateTimeField(auto_now_add=True)

    orderStatus = models.CharField(choices=ORDER_STATUS, max_length=1024, default=ORDER_STATUS_UPCOMING)

    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()

    is_deleted = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'orders'

    @staticmethod
    def get_object_or_raise_exception(order_id):
        try:
            return Orders.objects.get(pk=ObjectId(order_id))
        except Orders.DoesNotExist:
            response = {
                'success': False,
                'detail': f'Order with id {order_id} does not exist'
            }
            raise InvalidProfileException(response, status_code=status_codes.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get_object_or_none(order_id):
        try:
            return Orders.objects.get(pk=ObjectId(order_id))
        except Orders.DoesNotExist:
            return None

    def delete_order(self):
        self.is_deleted = True
        self.save()

    def save(self, *args, **kwargs):

        current_time = datetime.now()

        if not self.createdAt:
            self.createdAt = current_time

        self.updatedAt = current_time

        super(Orders, self).save(*args, **kwargs)

class Coupons(models.Model):
    objects = models.DjongoManager()

    _id = models.ObjectIdField(primary_key=True)
    name = models.TextField()
    description = models.TextField()

    validity = models.JSONField()

    couponDetail = models.JSONField()

    vendorId = models.TextField()

    category = models.CharField(choices=COUPON_STATES, max_length=1024, default=COUPON_STATE_ACTIVE)
    count = models.IntegerField(default=0)
    maxCount = models.IntegerField(null=True)
    minAmount = models.IntegerField(null=True)

    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()

    is_deleted = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'coupons'

    @staticmethod
    def get_object_or_raise_exception(coupon_id):
        try:
            return Coupons.objects.get(pk=ObjectId(coupon_id))
        except Coupons.DoesNotExist:
            response = {
                'success': False,
                'detail': f'Coupon with id {coupon_id} does not exist'
            }
            raise InvalidProfileException(response, status_code=status_codes.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get_object_or_none(coupon_id):
        try:
            return Coupons.objects.get(pk=ObjectId(coupon_id))
        except Coupons.DoesNotExist:
            return None

    def delete_coupon(self):
        self.is_deleted = True
        self.save()

    def save(self, *args, **kwargs):

        current_time = datetime.now()

        if not self.createdAt:
            self.createdAt = current_time

        self.updatedAt = current_time

        super(Coupons, self).save(*args, **kwargs)

class Payments(models.Model):
    objects = models.DjongoManager()

    _id = models.ObjectIdField()
    status = models.CharField(choices=PAYMENT_STATUS, max_length=1024, default=PAYMENT_STATUS_PENDING)
    amount = models.IntegerField()
    details = models.TextField()

class Categories(models.Model):
    objects = models.DjongoManager()

    _id = models.ObjectIdField()
    name = models.CharField(max_length=255, null=False)

    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()

    is_deleted = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'categories'

    @staticmethod
    def get_object_or_raise_exception(category_id):
        try:
            return Categories.objects.get(pk=ObjectId(category_id))
        except Categories.DoesNotExist:
            response = {
                'success': False,
                'detail': f'Category with id {category_id} does not exist'
            }
            raise InvalidProfileException(response, status_code=status_codes.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get_object_or_none(category_id):
        try:
            return Categories.objects.get(pk=ObjectId(category_id))
        except Categories.DoesNotExist:
            return None

    def delete_category(self):
        self.is_deleted = True
        self.save()

    def save(self, *args, **kwargs):

        current_time = datetime.now()

        if not self.createdAt:
            self.createdAt = current_time

        self.updatedAt = current_time

        super(Categories, self).save(*args, **kwargs)
