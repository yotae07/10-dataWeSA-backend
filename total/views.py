from django.http  import JsonResponse
from django.views import View
from total.models import Total

class TotalView(View):
    def get(self, response):
        total_data = Total.objects.all()
        data = [{
            'title'   : total.title,
            'value'   : total.value,
            'subTitle': total.sub_title
        } for total in total_data]
        return JsonResponse({'stat': data}, status=200)