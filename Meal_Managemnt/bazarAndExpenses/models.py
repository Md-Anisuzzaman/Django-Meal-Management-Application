from django.db import models
from account.models import Account

class DailyBazars(models.Model):
    bazar_date = models.DateField()
    item_name = models.CharField(max_length=255)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bazar_total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(null=True,default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.item_name 

