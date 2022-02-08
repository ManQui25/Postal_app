from main_app.models import Postal
from rest_framework import serializers


class PostalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postal
        fields = ['id','lat', 'lon']

def to_representation(self, obj):
    post = Postal.objects.get(id=obj.id)

    return{
        'id' : obj.id,
        'lat' : obj.lat,
        'lon' : obj.lon,
    } 