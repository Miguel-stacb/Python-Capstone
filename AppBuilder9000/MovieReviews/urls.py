from django.urls import path
from . import views


app_name = 'MovieReviews'

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('index/',views.index, name='index'),
    path('create/', views.create_movie, name='create_movie'),
    path('items/', views.items_list, name='items_list'),
    path('item/<int:item_id>/', views.item_details, name='item_details'),
    path('item/<int:item_id>/edit/', views.item_edit, name='item_edit'),
    path('item/<int:item_id>/delete/', views.item_delete, name='item_delete'),
]
