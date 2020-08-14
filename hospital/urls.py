from django.urls import path

from .views      import(
    BedView,
    IcuView
)

urlpatterns = [
    path('bed', BedView.as_view()),
    path('icu', IcuView.as_view())
]
