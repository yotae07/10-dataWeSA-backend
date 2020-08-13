import jwt
import json
import unittest

from django.test   import (
    Client,
    TestCase
)
from unittest.mock import (
    patch,
    MagicMock
)

from user.models   import (
    User,
    SocialMedia
)

class KakaoSuccessTest(TestCase):
    def setUp(self):
        social = SocialMedia.objects.create(name='kakao')

    def tearDown(self):
        SocialMedia.objects.all().delete()
        User.objects.all().delete()

    @patch('user.views.requests')
    def test_kakao_signin_success(self, mocked_requests):
        class FakeResponse:
            def json(self):
                return {'id': 12345, 'connected_at': '2020-01-01T00:00:00Z'}
        mocked_requests.get = MagicMock(return_value = FakeResponse())

        c      = Client()
        header = {'HTTP_Authorization':'fake_token.1234'}

        response = c.get('/kakao', content_type='applications/json', **header)
        self.assertEqual(response.status_code, 200)

class KakaoFailTest(TestCase):
    def setUp(self):
        social = SocialMedia.objects.create(name='kakao')

    def tearDown(self):
        SocialMedia.objects.all().delete()
        User.objects.all().delete()

    @patch('user.views.requests')
    def test_kakao_signin_fail(self, mocked_requests):
        class FakeResponse:
            def json(self):
                return {'request': 'INVALID_TOKEN', 'connected_at': '2020-01-01T00:00:00Z'}
        mocked_requests.get = MagicMock(return_value = FakeResponse())

        c      = Client()
        header = {'HTTP_Authorization': 'fake_token.1234'}

        response = c.get('/kakao', content_type='applications/json', **header)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {'message': 'KEY_ERROR'})

class GoogleSuccessTest(TestCase):
    def setUp(self):
        social = SocialMedia.objects.create(name='google')

    def tearDown(self):
        SocialMedia.objects.all().delete()
        User.objects.all().delete()

    @patch('user.views.requests')
    def test_google_signin_success(self, mocked_requests):
        class FakeResponse:
            def json(self):
                return {'sub': 12345, 'connected_at': '2020-01-01T00:00:00Z'}
        mocked_requests.get = MagicMock(return_value = FakeResponse())

        c      = Client()
        header = {'HTTP_Authorization':'fake_token.1234'}

        response = c.get('/google', content_type='applications/json', **header)
        self.assertEqual(response.status_code, 200)

class GoogleFailTest(TestCase):
    def setUp(self):
        social = SocialMedia.objects.create(name='google')

    def tearDown(self):
        SocialMedia.objects.all().delete()
        User.objects.all().delete()

    @patch('user.views.requests')
    def test_google_signin_fail(self, mocked_requests):
        class FakeResponse:
            def json(self):
                return {'request': 'INVALID_TOKEN', 'connected_at': '2020-01-01T00:00:00Z'}
        mocked_requests.get = MagicMock(return_value = FakeResponse())

        c      = Client()
        header = {'HTTP_Authorization':'fake_token.1234'}

        response = c.get('/google', content_type='applications/json', **header)
        self.assertEqual(response.status_code, 401)
