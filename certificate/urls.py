"""certificate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from status.views import get_status
from generate.views import certificate
from authorize.views import authorize
from agentkeys.views import getkey
from byphone.views import phone


urlpatterns = [
    path('admin/', admin.site.urls),
    path('status/', get_status),
    path('form/',certificate),
    path('',authorize,name='index'),
    path('key/',getkey),
    path('dd/',phone),
]
