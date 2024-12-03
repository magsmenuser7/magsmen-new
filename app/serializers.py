
from rest_framework import serializers
from .models import IntalksForm

class IntalksFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntalksForm
        fields = ['id', 'Intalk_Name', 'Intalk_Email', 'Intalk_Contact', 'Intalk_City', 'Intalk_Reason_to_connect']