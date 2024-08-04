from django.shortcuts import render
from rest_framework.views import APIView
from .models import FoodListSerializer, Food


class FoodListAPIView(APIView):
    def get(self, request):
        categories = Food.objects.filter(is_publish=False).distinct()

        serializer = FoodListSerializer(categories, many=True)

        return render(
            request,
            template_name='rest_framework/api.html',
            context={'categories': serializer.data}
        )
