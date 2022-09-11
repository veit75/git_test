from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='blog-home'),
    path('uebung', views.gut_uebung_11_9, name='test_gut')
]