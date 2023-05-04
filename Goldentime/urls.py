"""Goldentime URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from baseapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('/',views.into_index),
    path('',views.into_index),
    path('index',views.into_index),
    path('upload/',views.into_upload),
    path('login/',views.login),
    path('search/<str:searchname>',views.search),
    path('mylove/',views.into_mylove),
    path('mypost/',views.into_mypost),
    path('into_sigin/',views.into_sigin),
    path('logout/',views.logout),
    path('into_login/',views.login),
]
