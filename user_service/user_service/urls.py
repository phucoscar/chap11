"""user_service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from user_model import views as v_model
from user_login import views as v_login
from user_info import views as v_info
urlpatterns = [
    path('admin/', admin.site.urls),
    path('userregistration/', v_model.registration_req),
    path('userlogin/', v_login.user_login),
    path('userinfo/',v_info.user_info)
]
