import json

from django.http  import JsonResponse
from django.views import View

from daily.models import State
from .models      import (
    Place,
    Mobility
)

class MobilityView(View):
    def get(self, request):
        place_name = request.GET.get('place')
        try:
            if place_name:
                datas  = State.objects.filter(mobility__place=Place.objects.get(name=place_name)).distinct()
                result = [
                    {
                        "name": data.name,
                        "data": list(
                            data.mobility_set.filter(
                                state=data.id,
                                place=Place.objects.get(name=place_name)
                                ).values_list("visit_rate", flat=True)
                            )
                    } for data in datas]
                return JsonResponse({'series': result}, status=200)
            return JsonResponse({'message': 'INVALID_REQUEST'}, status=401)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=401)
