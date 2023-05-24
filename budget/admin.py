from django.contrib import admin
from .models import UserModel, ExpenseModel

admin.site.register(UserModel)
admin.site.register(ExpenseModel)
# Register your models here.
