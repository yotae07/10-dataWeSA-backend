from django.urls import path

from .views      import (
    MobilityView
)

urlpatterns = [
    path('mobility', MobilityView.as_view())
]

