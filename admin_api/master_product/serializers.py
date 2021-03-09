import json
from collections import OrderedDict  # don't remove this import
from rest_framework import serializers
from ..models import MasterProduct


class MasterProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = MasterProduct
        fields = '__all__'

