from django.db import models



class Restaurant(models.Model):
    # rest_id = models.Column(models.Integer, primary_key=True, autoincrement=True)
    # name = models.Column(models.String, nullable=False)
    # address = models.Column(models.String, nullable=False)
    # dish = models.relationship("Dish", back_populates="restaurant")

    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

class Dish(models.Model):
    # dish_id = models.Column(models.Integer, primary_key=True, autoincrement=True)
    # name = models.Column(models.String, nullable=False)
    # rating = models.Column(models.Integer, nullable=True)
    # rest_id = models.Column(models.Integer, models.ForeignKey('models.rest_id'), nullable=False)
    # restaurant = models.relationship("Restaurant", back_populates="dishes")

    name = models.CharField(max_length=200)
    rating = models.IntegerField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)   