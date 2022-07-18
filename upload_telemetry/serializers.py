from .models import InstrumentModels
from rest_framework import serializers


class InstrumentSerializer(serializers.ModelSerializer):
    """
    model :
    fields : 命名固定使用此，用以決定能存進資料庫的欄位
    exclude : 反向資料庫欄位
    """

    class Meta:
        model = InstrumentModels

        # fields = '__all__'
        fields = ["ip_address", "serial_number", 'temperature', 'humidity']

