import json

from django.http    import JsonResponse
from django.views   import View

from user.utils     import LoginConfirm
from product.models import Product
from .models        import (
    Order
)

class OrderView(View):
    @LoginConfirm
    def post(self, request):
        try:
            data = json.loads(request.body)
            if data['item']:
                for state_id in data['item']:
                    if Order.objects.filter(user = request.user, product= Product.objects.get(id=state_id)).exists():
                        pass
                    else:
                        Order.objects.create(
                            user = request.user,
                            product = Product.objects.get(id=stae_id)
                        )
                user_items = Order.objects.select_related('product').filter(id=request.user.id).order_by('product')
                result = [
                    {
                        "id": user_item.product.id,
                        "auth": True,
                        "title": user_item.product.name,
                        "src": user_item.product.image,
                        "link": user_item.product.url
                    }for user_item in user_items]
                return JsonResponse({'message': result}, status=200)
            return JsonResponse({'message': 'INVALID_REQUEST'}, status=400)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=401)

