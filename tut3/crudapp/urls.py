from django.urls import path
from .views import get_details, post_details, post_detail

urlpatterns = [
    path('details/', get_details, name='get_details'),
    path('details/post', post_details, name='post_details'),
    path('details/<int:pk>', post_detail, name='post_detail'),
]