from django.db import transaction
from django.http import JsonResponse

from rest_framework.generics import GenericAPIView

from upload_telemetry.models import InstrumentModels
from upload_telemetry.serializers import InstrumentSerializer


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
        """
        request_data = request.data
        serializer = self.serializer_class(data=request_data)
        if serializer.is_valid() is False:
            return JsonResponse({"status": "fail"})

        try:
            with transaction.atomic():
                serializer.save()
                return JsonResponse({"status": "success"})

        except Exception as e:
            return JsonResponse({"status": e})

