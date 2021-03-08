import json
from collections import OrderedDict  # don't remove this import
from rest_framework import serializers
from ..models import Categories


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = '__all__'

    def to_representation(self, category):
        data = super(CategorySerializer, self).to_representation(category)
        fields = self._readable_fields

        for field in fields:

            if data[field.field_name] is None:
                del data[field.field_name]

        return data