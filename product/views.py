import json

from django.http  import JsonResponse
from django.views import View

from .models      import (
    Occupation,
    Year,
    Race,
    Chart,
    Graph,
    Product
)

class ChartView(View):
    def get(self, request):
        total      = 9652535
        chart_data = Chart.objects.select_related('occupation', 'group').order_by('group')
        result     = [
            {
                "group"        : data.group.group,
                "name"         : data.occupation.name,
                "year"         : 2018,
                "value"        : str((data.people/total)*100),
                "people"       : data.people,
                "average_wage" : data.salary
            } for data in chart_data]
        return JsonResponse({'data': result}, status=200)

class GraphView(View):
    def get(self, request):
        graph_data = Race.objects.prefetch_related('graph_set').order_by('id')[:4]
        result     = [
            {
                "name": data.race,
                "data": list(data.graph_set.values_list('salary', flat=True))
            } for data in graph_data]
        return JsonResponse({'data': result}, status=200)

class ProductView(View):
    def get(self, request):
        product_data = list(Product.objects.all())
        result       = [
            {
                "id"    : data.id,
                "title" : data.name,
                "src"   : data.image,
                "link"  : data.url
             } for data in product_data]
        return JsonResponse({'message': result}, status=200)
