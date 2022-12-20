from django.contrib import admin
from django.urls import path
from celleng.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home,name="home"),
    path('form/', form,name="form"),
]
