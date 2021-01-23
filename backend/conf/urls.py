"""conf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from rest_framework_jwt.views import (
    obtain_jwt_token,
    refresh_jwt_token,
    verify_jwt_token,
)


jwt_urls = [
    path("obtain", obtain_jwt_token, name="jwt-obtain"),
    path("refresh", refresh_jwt_token, name="jwt-refresh"),
    path("verify", verify_jwt_token, name="jwt-verify"),
]


api_urls = [
    path("", include("rest_framework.urls")),
    path("jwt/", include(jwt_urls)),
]


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(api_urls)),
]
