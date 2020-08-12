from django.test  import TestCase
from total.models import (
    Total
)

class TotalTestCase(TestCase):
    def setUp(self):
        total = Total(
            title     ='Confirmed Cases',
            value     ='5,116,474',
            sub_title ='in the USA',
            is_deleted=False
        )
        total.save()
    def tearDown(self):
        Total.objects.all().delete()

    def test_total_success(self):
        total_response = self.client.get('/total')
        self.assertEqual(total_response.status_code, 200)

    def test_total_fail(self):
        total_response = self.client.get('/totalll')
        self.assertEqual(total_response.status_code, 404)