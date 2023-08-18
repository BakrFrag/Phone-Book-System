from rest_framework import serializers 
from contact.models import Contact , PhoneNumber
from django.db import transaction


class PhoneNumberSerializer(serializers.ModelSerializer):
    """
    serializing phone number models
    """
  
    class Meta:
        model= PhoneNumber
        fields=["id","number"]

    