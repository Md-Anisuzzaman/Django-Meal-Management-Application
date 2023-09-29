from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account, UserPayment,Settings


class AccountAdmin(UserAdmin):
    list_display = ('id', 'email', 'username', 'mobile', 'role', 'department', 'created_at',
                    'updated_at', 'last_login',)
    list_display_links = ('email',)
    readonly_fields = ('created_at', 'updated_at',)
    ordering = ('-created_at',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)


class UserPaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'month', 'payment_date', 'status',  'creator', 'created_at',
                    'updated_at')
    list_display_links = ('user',)
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(UserPayment, UserPaymentAdmin)


class SettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'contact_name', 'contact_number', 'meal_set_last_time', 'meal_set_alert_time',
                    'today_meal_coocking_start_time', 'today_meal_coocking_end_time', 'shut_down_app', 'shut_down_reason', 'alert_text_for_all')
    list_display_links = ('id',)


admin.site.register(Settings,SettingsAdmin)
