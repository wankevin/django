"""kevin_webserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from real_time_system import views
from kevin_webserver.consumer import ChatConsumer

urlpatterns = [
    path('', views.view),
    path('test', views.get_late_data_from_database1)

]

websocket_urlpatterns = [
    path('ws/online_number/', ChatConsumer),
]

