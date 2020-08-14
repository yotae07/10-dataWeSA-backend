from django.urls import path

from daily.views import DailyView, SearchDailyView

urlpatterns = [
    path('', DailyView.as_view()),
    path('/<str:state_id>', SearchDailyView.as_view()),
]
