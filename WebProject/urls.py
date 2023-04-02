"""WebProject URL Configuration

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
from django.urls import path
from WebApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('about/',about),
    path('abhay/',abhay),
    # path('showdata/',showdata,name='showdata'),
    #path('getdata/<int:id>',getdata,name=getdata)
    path('getformdata/',getformdata,name='getformdata'),
    path('result/',result,name='result'),
    path('form/',getdata_form,name="form"),
    path('getdata_db/',getdata_db,name="getdata_db"),
    path('getdetail/<int:id>',getdetail,name="getdetail"),
    path('signup/',create,name="create"),
    path('update/<int:id>',update,name="update"),
    path('delete/<int:id>',delete,name="delete"),
    path('movies/',movies,name="movies"),
    path('set_cookies/',set_cookie,name="set_cookies"),
    path('get_cookies/',get_cookie,name="get_cookies"),
    path('del_cookies/',del_cookie,name="del_cookies")
    
]
