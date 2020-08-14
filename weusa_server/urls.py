"""weusa_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include

urlpatterns = [
    path('daily', include('daily.urls')),
    path('', include('cart.urls')),
    path('', include('hospital.urls')),
    path('', include('mobility.urls')),
    path('user', include('user.urls')),
    path('', include('product.urls')),
    path('crawling', include('crawling.urls')),
    path('total', include('total.urls'))
]
