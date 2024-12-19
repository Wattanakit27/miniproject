from django.urls import path
from . import views  # Import views จาก accounts

urlpatterns = [
    path('', views.home_view, name='home'),  # URL สำหรับหน้าแรก
    path('second/', views.second_view, name='second'),  # URL สำหรับหน้าที่สอง
]
