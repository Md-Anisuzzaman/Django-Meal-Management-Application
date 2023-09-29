from django.contrib import admin
from account_logs.models import AccountLogs

class AccountLogsAdmin(admin.ModelAdmin):
    list_display = ('id','creator','amount','income_date', 'is_expense','is_income','exp_category','status','created_at', 'updated_at')
    list_display_links = ('id',)

admin.site.register(AccountLogs,AccountLogsAdmin)
    
