from django.db import models


# Create your models here.
class InstrumentModels(models.Model):
    ip_address = models.CharField(max_length=20)  # adam ip address位址
    serial_number = models.CharField(max_length=20)  # serial number
    temperature = models.IntegerField()
    humidity = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)

