import datetime
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from upload_telemetry.models import InstrumentModels


def view(request, room_name):
    # data = InstrumentModels.objects.latest("serial_number")
    # data = get_late_data_from_database(_filter="asdds5003")
    return render(request, "show.html", locals())


def get_late_data_from_database(_filter: str):
    data_list = InstrumentModels.objects.filter(serial_number=_filter)
    return data_list[len(data_list) - 1]


def get_late_data_from_database1(request):
    data_list = InstrumentModels.objects.filter(serial_number="asdds5003")
    data = data_list[len(data_list) - 1]
    datetime_now = datetime.datetime.now()
    return JsonResponse({'temperature': data.temperature, 'humidity': data.humidity, "datetime": str(datetime_now)},
                        safe=False)
