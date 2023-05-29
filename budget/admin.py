from django.contrib import admin

from .models import ExpenseModel, Wallet, IncomeModel

admin.site.register(ExpenseModel)
admin.site.register(Wallet)
admin.site.register(IncomeModel)
