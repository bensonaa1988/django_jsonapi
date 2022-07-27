from urllib import response
from django.shortcuts import render
from opinion_ate import serializers

# Create your views here.
from opinion_ate.models import Restaurant, Dish
from opinion_ate.serializers import RestaurantSerializer, DishSerializer
from rest_framework import viewsets

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def get_list_Restaurant(self):
        return Restaurant.objects.filter(id=self.request.user.pk)

    def perform_create(self, serializer):
        serializer.save(id=self.request.user)    


class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    def get_list_dish(self):
        return Dish.objects.filter(id=self.request.user.pk)
    def perform_create(self, serializer):
        serializer.save(id=self.request.user)     