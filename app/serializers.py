
from rest_framework import serializers
from .models import IntalksForm

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntalksForm
        fields = ['id', 'Name', 'Email', 'Contact', 'City', 'Reason_to_connect']