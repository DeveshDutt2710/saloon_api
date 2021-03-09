import json
from collections import OrderedDict  # don't remove this import
from rest_framework import serializers
from ..models import Account


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = '__all__'

