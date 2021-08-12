from api.models import Schemes
from rest_framework import serializers
from django.db import models

# Serializers allow complex data to Python datatypes that can then be easily rendered into JSON

class SchemesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Schemes
        fields = ["code", "scheme"]



