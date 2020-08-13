from django.urls import path

from .views      import (
    KakaoSignIn,
    GoogleSignIn
)

urlpatterns = [
    path('/kakao', KakaoSignIn.as_view()),
    path('/google', GoogleSignIn.as_view())
]

