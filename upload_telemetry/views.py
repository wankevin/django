from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# def hello_world(request: WSGIRequest):
#     """
#     requests : upload_telemetry.urls.py 轉過來的資料
#     """
#     return HttpResponse("Hello World!")


from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from upload_telemetry.models import InstrumentModels
from upload_telemetry.serializers import InstrumentSerializer


class InstrumentViews(viewsets.ModelViewSet):
    queryset = InstrumentModels.objects.all()
    serializer_class = InstrumentSerializer
    permission_classes = (AllowAny,)
