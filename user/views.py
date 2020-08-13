import json
import jwt
import requests

from django.views            import View
from django.http             import JsonResponse

from .models                 import (
    User,
    SocialMedia
)

from weusa_server.settings   import (
    SECRET_KEY,
    ALGORITHM
)

class KakaoSignIn(View):
    def get(self, request):
        try:
            access_token = request.headers["Authorization"]
            headers      = ({'Authorization' : f"Bearer {access_token}"})
            url          = "https://kapi.kakao.com/v2/user/me"
            response     = requests.get(url, headers=headers)
            user         = response.json()

            if User.objects.filter(user = str(user['id'])).exists():
                user_info   = User.objects.get(user=str(user['id']))
                encoded_jwt = jwt.encode({'id': user_info.id}, SECRET_KEY, ALGORITHM).docode('utf-8')

                return JsonResponse({'access_token' : encoded_jwt}, status = 200)            
            new_user_info = User(
                user    = str(user['id']),
                social  = SocialMedia.objects.get(name='kakao')
            )
            new_user_info.save()
            encoded_jwt = jwt.encode({'id': new_user_info.id}, SECRET_KEY, ALGORITHM).decode('utf-8')
            return JsonResponse({'access_token' : encoded_jwt}, status = 200)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=401)


class GoogleSignIn(View):
    def get(self, request):
        try:
            token    = request.headers["Authorization"]
            url      = "https://oauth2.googleapis.com/tokeninfo?id_token="
            response = requests.get(url+token)
            user     = response.json()
            
            if User.objects.filter(user = user['sub']).exists():
                user_info = User.objects.get(user=user['sub'])
                token     = jwt.encode({'id': user_info.id}, SECRET_KEY, ALGORITHM).decode('utf-8')
                return JsonResponse({'token': token}, status = 200)
            user_info = User(
                user    = user['sub'],
                social  = SocialMedia.objects.get(name ="google")
            )
            user_info.save()
            token = jwt.encode({'id': user_info.id}, SECRET_KEY, ALGORITHM).decode('utf-8')
            return JsonResponse({'token': token}, status = 200)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=401)
