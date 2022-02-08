import csv
from django.shortcuts import render
from rest_framework   import generics, status

from django.http import HttpResponse
from rest_framework.response import Response
from main_app.models import Postal
from main_app.serializers import PostalSerializer

def import_csv(request):
    coordenadas = []
    with open("postcodesgeo.csv", "r") as csv_file:
        data = list(csv.reader(csv_file, delimiter=","))
        for row in data[1:]:
            coordenadas.append(
                Postal(
                    lat = row[0],
                    lon = row[1],
                )
            )
    if len(coordenadas) > 0:
        Postal.objects.bulk_create(coordenadas)
    
    return HttpResponse("Successfully imported")

class PostalView(generics.ListAPIView):
    queryset = Postal.objects.all()
    serializer_class = PostalSerializer

    def get_queryset(self):
        queryset = Postal.objects.filter(id=self.kwargs['id'])
        return queryset

    
