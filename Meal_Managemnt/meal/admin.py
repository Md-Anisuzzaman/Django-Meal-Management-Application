from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserMeals, MonthlyMeals, MealMenus


class UserMealsAdmin(admin.ModelAdmin):
    list_display = ('id', 'creator', 'quantity', 'date',
                    'status', 'created_at', 'updated_at')
    list_display_links = ('creator',)


admin.site.register(UserMeals, UserMealsAdmin)


class MonthlyMealsAdmin(admin.ModelAdmin):
    list_display = ('id', 'creator', 'meal_rate', 'month_start_date',
                    'month_end_date', 'is_visible', 'status', 'created_at', 'updated_at')
    list_display_links = ('id',)
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(MonthlyMeals, MonthlyMealsAdmin)


class MonthlyMealsAdmin(admin.ModelAdmin):
    list_display = ('id', 'creator', 'date', 'recipe', 'description',
                    'status', 'created_at', 'updated_at')
    list_display_links = ('id',)
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(MealMenus, MonthlyMealsAdmin)
