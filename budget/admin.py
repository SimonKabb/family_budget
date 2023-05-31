from django.contrib import admin

from .models import ExpenseModel, Wallet, IncomeModel, CategoryModel

admin.site.register(ExpenseModel)
admin.site.register(Wallet)


@admin.register(IncomeModel)
class IncomeModelAdmin(admin.ModelAdmin):
    list_display = ['amount_of_income', 'date', 'description']
    empty_value_display = "-empty-"


admin.site.register(CategoryModel)
