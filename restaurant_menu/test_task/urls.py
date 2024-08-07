from django.urls import path
from test_task.views import FoodListAPIView


urlpatterns = [
    path('foods/', FoodListAPIView.as_view(), name='food-list')
]
