from django.urls    import path

from crawling.views import (
    TotalCrawlingView,
    HospitalCrawlingView,
    DailyCrawlingView,
    MobilityCrawlingView,
    ElementCrawlingView,
    ProductCrawlingView
)

urlpatterns = [
    path('/total', TotalCrawlingView.as_view()),
    path('/daily', DailyCrawlingView.as_view()),
    path('/element', ElementCrawlingView.as_view()),
    path('/mobility', MobilityCrawlingView.as_view()),
    path('/hospital', HospitalCrawlingView.as_view()),
    path('/product', ProductCrawlingView.as_view()),
]
