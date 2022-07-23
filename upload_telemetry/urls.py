from django.urls import path, include
from rest_framework.routers import DefaultRouter

from upload_telemetry.views import *

urlpatterns = [
    path('', InstrumentViews.as_view())
]
