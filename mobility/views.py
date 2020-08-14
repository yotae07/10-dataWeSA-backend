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
        state_name = request.GET.get('state')
        if state_name == None:
            states = None
        else:
            states = state_name.split(',')
        try:
            if place_name:
                datas = State.objects.filter(mobility__place=Place.objects.get(name=place_name)).distinct()
                if states != None:
                    select_state = [State.objects.get(id=data.id) for data in datas if str(data.id) in states]
                    result = [
                        {
                            "id"  : state.id,
                            "name": state.name,
                            "data": list(
                                state.mobility_set.filter(
                                    state=state.id,
                                    place=Place.objects.get(name=place_name))
                                    .values_list("visit_rate", flat=True)
                                )
                        } for state in select_state]
                else:
                    result = [
                        {
                            'id'   : data.id,
                            'name' : data.name,
                            'data' : list(
                                data.mobility_set.filter(
                                    state = data.id,
                                    place = Place.objects.get(name=place_name))
                                    .values_list('visit_rate', flat=True)
                                )
                        } for data in datas]
                return JsonResponse({'series': result}, status=200)
            return JsonResponse({'message': 'INVALID_REQUEST'}, status=401)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=401)
        except Place.DoesNotExist:
            return JsonResponse({'message': 'NOT_EXISTS'}, status=401)

