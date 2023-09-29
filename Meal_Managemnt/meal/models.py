from django.db import models
from account.models import Account


class UserMeals(models.Model):
    date = models.DateField(null=True)
    quantity = models.IntegerField(null=True,default=1)
    status = models.BooleanField(null=True,default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    creator = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'User Meals'
        verbose_name_plural = 'User Meals'

class MonthlyMeals(models.Model):
    date = models.DateTimeField(null=True, blank=True)
    meal_rate = models.DecimalField(max_digits=10, decimal_places=2)
    is_visible = models.BooleanField(default=False)
    month_start_date = models.DateTimeField(null=True, blank=True)
    month_end_date = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(null=True,default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Monthly Meals"
        verbose_name_plural = "Monthly Meals"

class MealMenus(models.Model):
    date = models.DateField(null=True, blank=True)
    recipe = models.TextField()
    description = models.TextField()
    status = models.BooleanField(null=True,default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Meal Menus"
        verbose_name_plural = "Meal Menus"

