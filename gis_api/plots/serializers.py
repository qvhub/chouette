from rest_framework import serializers
from django.contrib.gis.geos import Polygon
from .models import Plot
from accounts.serializers import UserRegisterSerializer



class PlotListSerializer(serializers.ModelSerializer):
    # zone = PolygonField()
    area_hectares = serializers.SerializerMethodField()
    user = UserRegisterSerializer()

    class Meta:
        model = Plot
        fields = ['id', 'name', 'zone', 'area_hectares', 'user']
        read_only_fields =['area_hectares']

    def get_area_hectares(self, obj):
        return obj.area_in_hectares()

class PlotSerializer(serializers.ModelSerializer):
    area_hectares = serializers.SerializerMethodField()

    class Meta:
        model = Plot
        fields = ['id', 'name', 'zone', 'area_hectares', 'user']
        read_only_fields =['area_hectares']

    def get_area_hectares(self, obj):
        return obj.area_in_hectares()
