
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard,name="dashboard"),
    path('create/', views.create,name="create"),
    path('getProducts/', views.getProducts,name="getProducts"),
]
