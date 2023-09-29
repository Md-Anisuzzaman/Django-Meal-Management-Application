from django.db import models
from account.models import Account
from expense_category.models import ExpenseCategory

class AccountLogs(models.Model):
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    is_expense = models.BooleanField(default=False)
    is_income = models.BooleanField(default=False)
    income_date = models.DateField(null=True, blank=True)
    exp_category = models.ForeignKey(ExpenseCategory,on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    creator = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True, related_name='created_account_logs')

    class Meta:
        verbose_name = 'account_logs'
        verbose_name_plural = 'account Logs'

 
