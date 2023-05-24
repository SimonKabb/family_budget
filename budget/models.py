from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class CategoryModel(models.Model):
    category_name = models.TextField()
    description = models.TextField()


class ExpenseModel(models.Model):
    amount_of_outcome = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    cathegory = models.ForeignKey(
        CategoryModel, on_delete=models.SET_NULL, null=True)


class IncomeModel(models.Model):
    amount_of_income = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    cathegory = models.ForeignKey(
        CategoryModel, on_delete=models.SET_NULL, null=True)


class GoalModel(models.Model):
    goal_name = models.TextField
    description = models.TextField
    author = models.ForeignKey(User, on_delete=models.CASCADE)
