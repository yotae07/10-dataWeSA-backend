import json

from django.test  import (
    TestCase,
    Client
)

from daily.models import State
from .models import (
    Icu,
    Bed
)

class BedTest(TestCase):
    def setUp(self):
        state = State.objects.create(
            name = 'Alaska',
            populations = 737438,
            is_deleted = 0
        )
        Bed.objects.create(
            state = state,
            beds_per_thousand = 2.00,
            is_deleted = 0
        )

    def tearDown(self):
        State.objects.all().delete()
        Bed.objects.all().delete()

    def test_bedview_testcase_success(self):
        
        response = self.client.get('/bed')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            'result': 'success',
            "data": [
                {
                    "id": 'Alaska',
                    'year': 2018,
                    'value': '2.00'
                }]})
    def test_bedview_testcase_fail(self):


        response = self.client.get('/beds')
        self.assertEqual(response.status_code, 404)

        
class IcuTest(TestCase):
    def setUp(self):
        state = State.objects.create(
            name = 'Alaska',
            populations = 737438,
            is_deleted = 0
        )
        Icu.objects.create(
            state= state,
            total = 217,
            total_per_capita = 0.29,
            is_deleted = 0
        )

    def tearDown(self):
        State.objects.all().delete()
        Icu.objects.all().delete()

    def test_icuview_testcase_success(self):
        response = self.client.get('/icu')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            'result': 'success',
            'data': [
                {
                    "id": "Alaska",
                    "total": 217,
                    "result": "0.29"
                }]})


    def test_icuview_testcase_fail(self):
        response = self.client.get('/icus')
        self.assertEqual(response.status_code, 404)
