from django.contrib import admin
from django.urls import path, include
import home.views
import lectures.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.views.home, name='home'),\
]
