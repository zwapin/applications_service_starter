# IMPORTING THIRD PARTY PACKAGES
from django.apps import apps
from rest_framework import serializers


class StoreInputSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    city = serializers.CharField(max_length=100)


class StoreSerializerModel(serializers.ModelSerializer):

    class Meta:
        model = apps.get_model("django_db_models", "StoreModel")
        fields = ["id", "name", "city"]
