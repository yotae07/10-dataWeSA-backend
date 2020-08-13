import json

from django.test  import (
    TestCase,
    Client
)

from .models      import (
    Group,
    Graph,
    Occupation,
    Year,
    Race,
    Chart,
    Product
)

class ChartViewTest(TestCase):
    def setUp(self):
        occupation = Occupation.objects.create(
            name       = "Recreation workers",
            is_deleted = 0
        )
        group = Group.objects.create(
            group      = "Service Occupations",
            is_deleted = 0
        )
        Chart.objects.create(
            group      = group,
            occupation = occupation,
            salary     = 10774,
            people     = 1268,
            is_deleted = 0
        )

    def tearDown(self):
        Chart.objects.all().delete()
        Occupation.objects.all().delete()
        Group.objects.all().delete()

    def test_chartview_testcase_success(self):

        response = self.client.get('/chart')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'data': [{
            "group"        : "Service Occupations",
            "name"         : "Recreation workers",
            "year"         : 2018,
            "value"        : "0.013136445503694107",
            "people"       : 1268,
            "average_wage" : 10774
        }]})

    def test_chartview_testcase_fail(self):

        response = self.client.get('/charts')
        self.assertEqual(response.status_code, 404)

class GraphViewTest(TestCase):
    def setUp(self):
        race = Race.objects.create(
            race       = "White",
            is_deleted = 0
        )
        Graph.objects.create(
            race       = race,
            people     = 523,
            salary     = 10774,
            is_deleted = 0
        )

    def tearDown(self):
        Race.objects.all().delete()
        Graph.objects.all().delete()

    def test_graphview_testcase_success(self):

        response = self.client.get('/graph')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'data': [{
            "name" : "White",
            "data" : [10774]
        }]})

    def test_graphview_testcase_fail(self):

        response = self.client.get('/graphs')
        self.assertEqual(response.status_code, 404)

class ProductViewTest(TestCase):
    def setUp(self):
        Product.objects.create(
            id         = 1,
            name       = "Department of Interior Spending by State",
            img        = "https://datausa.io/api/profile/geo/washington-dc/thumb",
            url        = "https://datausa.io/visualize?groups=0-Z1MxM8L&groups=1-1pz0Cl-14&measure=1e64mv",
            is_deleted = 0
        )

    def tearDown(self):
        Product.objects.all().delete()

    def test_productview_testcase_success(self):

        response = self.client.get('/product')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'message': [{
            "id"    : 1,
            "title" : "Department of Interior Spending by State",
            "src"   : "https://datausa.io/api/profile/geo/washington-dc/thumb",
            "link"  : "https://datausa.io/visualize?groups=0-Z1MxM8L&groups=1-1pz0Cl-14&measure=1e64mv"
        }]})

    def test_productview_testcase_fail(self):

        response = self.client.get('/products')
        self.assertEqual(response.status_code, 404)
