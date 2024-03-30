from django.urls import path
from .views import add_village, show_village, update_village, delete_village


urlpatterns = [
    path('add/', add_village, name='add_url'),
    path('show/', show_village, name='show_url'),
    path('update/<int:pk>/', update_village, name='update_url'),
    path('delete/<int:pk>/', delete_village, name='delete_url'),
]