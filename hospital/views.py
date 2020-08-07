from django.http  import JsonResponse
from django.views import View

from .models      import (
    Bed,
    Icu
)

class BedView(View):
    def get(self, request):
        bed_data = Bed.objects.select_related('state')
        data = [{
            'id'   : item.state.name,
            'year' : 2018,
            'value': item.beds_per_thousand,
        } for item in bed_data.all()]
        return JsonResponse({'result': 'success', 'data': data})

class IcuView(View):
    def get(self, request):
        icu_data = Icu.objects.select_related('state')
        data = [{
            'id'    : item.state.name,
            'total' : item.total,
            'result': item.total_per_capita
        }for item in icu_data.all()]
        return JsonResponse({'result': 'success', 'data': data})
