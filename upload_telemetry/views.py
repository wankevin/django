import json

from django.db import transaction
from django.http import JsonResponse

from rest_framework.generics import GenericAPIView
from upload_telemetry.models import InstrumentModels
from upload_telemetry.serializers import InstrumentSerializer

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

channel_layer = get_channel_layer()

ip_address_match_chat = {
    "192.168.1.101": "1",
    "192.168.1.102": "2",
}


class InstrumentViews(GenericAPIView):
    """
    InstrumentSerializer 將資料進行 序列化
    """
    queryset = InstrumentModels.objects.all()
    serializer_class = InstrumentSerializer

    def get(self, request):
        users = self.get_queryset()
        serializer = self.serializer_class(users, many=True)
        data = serializer.data
        return JsonResponse(data, safe=False)

    def post(self, request):
        """
        serializer.is_valid check data is model need
        with transaction.atomic()  發生錯誤時會rollback
        requests.data={"ip_address": "192.168.1.101", "serial_number": "asdds5003", "temperature": "22", "humidity": "53"}

        """

        request_data = request.data
        serializer = self.serializer_class(data=request_data)
        if serializer.is_valid() is False:
            return JsonResponse({"status": "fail"})

        try:
            # save data to database
            # with transaction.atomic():
            #     serializer.save()
            #     return JsonResponse({"status": "success"})

            # broadcast to front end
            data_json = eval(json.dumps(request.data))
            ip_address = data_json.get("ip_address")
            chat = ip_address_match_chat.get(ip_address)
            async_to_sync(channel_layer.group_send)(chat, {"type": "chat_message", "text": json.dumps(request.data)})
            return JsonResponse({"status": "success"})

        except Exception as e:
            return JsonResponse({"status": e})
