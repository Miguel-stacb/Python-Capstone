from django.urls import path
from . import views

app_name = 'MovieReviews'

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('index/',views.index, name='index'),
]
