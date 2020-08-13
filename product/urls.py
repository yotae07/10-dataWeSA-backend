from django.urls import path

from .views      import (
    ChartView,
    GraphView,
    ProductView
)

urlpatterns = [
    path('chart', ChartView.as_view()),
    path('graph', GraphView.as_view()),
    path('product', ProductView.as_view())
]