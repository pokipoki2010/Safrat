from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('details/', include('details.urls')),
    path('', views.homepage, name='home'),
]

