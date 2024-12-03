
from rest_framework import serializers
from .models import IntalksForm

class IntalksFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntalksForm
        fields = '__all__'