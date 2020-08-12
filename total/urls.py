from django.urls import path
from total.views import TotalView

urlpatterns = [
    path('', TotalView.as_view()),
]