from rest_framework import serializers
from django.contrib.gis.geos import Polygon
from .models import Plot

class PolygonField(serializers.Field):
    def to_representation(self, obj):
        return [{"lat": coord[1], "lng": coord[0]} for coord in obj[0]]

    def to_internal_value(self, data):
        try:
            coordinates = [( point["lng"], point["lat"]) for point in data]
        except KeyError:
            raise serializers.ValidationError("Invalid data format for zone")
        return Polygon(coordinates)


class ParcelSerializer(serializers.ModelSerializer):
    zone = PolygonField()
    area_hectares = serializers.SerializerMethodField()

    class Meta:
        model = Plot
        fields = ['id', 'name', 'zone', 'area_hectares']
        read_only_fields =['area_hectares']

    def get_area_hectares(self, obj):
        return obj.area_in_hectares()
