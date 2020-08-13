import json

from django.test  import (
    TestCase,
    Client
)

from daily.models import State
from .models      import (
    Mobility,
    Place
)

class MobilitySuccessTest(TestCase):
    def setUp(self):
        client = Client()
        state  = State.objects.create(
            name        = 'Alaska',
            populations = 737438,
            is_deleted  = 0
        )
        place = Place.objects.create(
            name       = 'Parks',
            is_deleted = 0
        )
        Mobility.objects.create(
            state      = state,
            place      = place,
            visit_rate = 202.0,
            is_deleted = 0
        )
    
    def tearDown(self):
        Mobility.objects.all().delete()
        Place.objects.all().delete()
        State.objects.all().delete()

    def test_mobilityview_testcase_success(self):

        response = self.client.get('/mobility', {'place': 'Parks'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"series": [
        {
            "name": "Alaska",
            "data": [202.0]
        }]})

class MobilityFailTest(TestCase):
    def setUp(self):
        client = Client()
        state = State.objects.create(
            name        = 'Alaska',
            populations = 737438,
            is_deleted  = 0
        )
        place = Place.objects.create(
            name       = 'Parks',
            is_deleted = 0
        )
        Mobility.objects.create(
            state      = state,
            place      = place,
            visit_rate = 202.0,
            is_deleted = 0
        )

    def tearDown(self):
        Mobility.objects.all().delete()
        Place.objects.all().delete()
        State.objects.all().delete()
    
    def test_mobilityview_testcase_fail(self):
        
        response = self.client.get('/mobility', {'place': 'Park'})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {'message': 'NOT_EXISTS'})

class MobilityFailTest2(TestCase):
    def setUp(self):
        client = Client()
        state  = State.objects.create(
            name        = 'Alaska',
            populations = 737438,
            is_deleted  = 0
        )
        place = Place.objects.create(
            name       = 'Parks',
            is_deleted = 0
        )
        Mobility.objects.create(
            state      = state,
            place      = place,
            visit_rate = 202.0,
            is_deleted = 0
        )

    def tearDown(self):
        Mobility.objects.all().delete()
        Place.objects.all().delete()
        State.objects.all().delete()
    
    def test_mobilityview_testcase_fail(self):
        
        response = self.client.get('/mobility', {'place': ''})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {'message': 'INVALID_REQUEST'})
