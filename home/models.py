from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class FoodType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Food(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=300)
    food_type = models.ForeignKey(FoodType, on_delete=models.CASCADE)


    def __str__(self):
        return self.name


class Comment(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()

    def __str__(self):
        return self.user.username