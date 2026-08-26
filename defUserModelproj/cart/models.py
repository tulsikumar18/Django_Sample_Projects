

from django.db import models
from django.contrib.auth.models import User

from menuapp.models import FoodItems


class CartItems(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='cart_items'
    )

    food_item = models.ForeignKey(
        FoodItems,
        on_delete=models.CASCADE,
        related_name='cart_items'
    )

    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} - {self.food_item.name}"