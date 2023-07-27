from rest_framework import serializers
from .models import Farmer, Field, Crop, Season


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = '__all__'


class FarmerSerializer(serializers.ModelSerializer):
    fields = FieldSerializer(many=True, read_only=True)

    class Meta:
        model = Farmer
        fields = '__all__'
