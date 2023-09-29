from django.contrib import admin
from expense_category.models import ExpenseCategory


class ExpenseCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'created_at', 'updated_at')
    list_display_links = ('category_name',)


admin.site.register(ExpenseCategory, ExpenseCategoryAdmin)
