import json
import jwt

from django.test           import (
    TestCase,
    Client
)

from weusa_server.settings import (
    SECRET_KEY,
    ALGORITHM
)

from user.models           import User, SocialMedia
from product.models        import Product
from .models               import Order

class OrderViewPostTest(TestCase):
    def setUp(self):
        client = Client()
        socialmedia = SocialMedia.objects.create(
            name = 'kakao',
            is_deleted = 0
        )
        user = User.objects.create(
            id = 1,
            user = '홍길동',
            social = socialmedia,
            is_deleted = 0
        )
        product = Product.objects.create(
            id = 1,
            name = "Department of Interior Spending by State",
            image = "https://datausa.io/api/profile/geo/washington-dc/thumb",
            url = "https://datausa.io/visualize?groups=0-Z1MxM8L&groups=1-1pz0Cl-14&measure=1e64mv",
            is_deleted = 0
        )
        Order.objects.create(
            user = user,
            product = product,
            is_deleted = 0
        )
    def tearDown(self):
        SocialMedia.objects.all().delete()
        User.objects.all().delete()
        Product.objects.all().delete()
        Order.objects.all().delete()

    def test_orderview_post_success(self):

        user = User.objects.get(id=1)
        token = jwt.encode({'id': user.id}, SECRET_KEY, ALGORITHM).decode('utf-8')
        header = {"HTTP_Authorization": token}
        item = {'item': [1]}

        response = self.client.post('/order', json.dumps(item), content_type='applications/json', **header)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": 
        [{
            "id": 1,
            "auto": True,
            "title": "Department of Interior Spending by State",
            "src": "https://datausa.io/api/profile/geo/washington-dc/thumb",
            "link": "https://datausa.io/visualize?groups=0-Z1MxM8L&groups=1-1pz0Cl-14&measure=1e64mv"
        }]})

    def test_orderview_test_fail(self):

        user = User.objects.get(id=1)
        token = jwt.encode({'id': user.id}, SECRET_KEY, ALGORITHM).decode('utf-8')
        header = {"HTTP_Authorization": token}
        item = {'item': []}

        response = self.client.post('/order', json.dumps(item), content_type='applications/json', **header)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": 'INVALID_REQUEST'})

    def test_orderview_test_except(self):

        user = User.objects.get(id=1)
        token = jwt.encode({'id': user.id}, SECRET_KEY, ALGORITHM).decode('utf-8')
        header = {"HTTP_Authorization": token}
        item = {'ite': [1]}

        response = self.client.post('/order', json.dumps(item), content_type='applications/json', **header)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {"message": 'KEY_ERROR'})

