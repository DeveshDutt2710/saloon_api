import json
from collections import OrderedDict  # don't remove this import
from rest_framework import serializers
from ..models import Coupons
import datetime


class CouponSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coupons
        fields = '__all__'

    def to_representation(self, coupon):
        data = super(CouponSerializer, self).to_representation(coupon)
        fields = self._readable_fields

        json_fields = ['couponDetail', 'validity']

        for field in fields:

            if field.field_name in json_fields and data[field.field_name] is not None:
                data[field.field_name] = dict(eval(data[field.field_name]))

            if data[field.field_name] is None:
                del data[field.field_name]

        return data