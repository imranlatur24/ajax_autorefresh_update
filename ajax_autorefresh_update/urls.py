
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard,name="dashboard"),
    path('student_data/', views.student_data,name="student_data"),
    path('create/', views.create,name="create"),
]
