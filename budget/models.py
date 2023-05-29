from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()
CURRENCY_LIST = [
    ('RUB', 'Russian Ruble'),
    ('USD', 'United States Dollar'),
    ('EUR', 'Euro'),
    ('JPY', 'Japanese Yen'),
    ('GBP', 'British Pound Sterling'),
    ('AUD', 'Australian Dollar'),
    ('CAD', 'Canadian Dollar'),
    ('CHF', 'Swiss Franc'),
    ('CNY', 'Chinese Yuan'),
    ('SEK', 'Swedish Krona'),
    ('NZD', 'New Zealand Dollar'),
    ('MXN', 'Mexican Peso'),
    ('SGD', 'Singapore Dollar'),
    ('HKD', 'Hong Kong Dollar'),
    ('NOK', 'Norwegian Krone'),
    ('KRW', 'South Korean Won')
]


class Wallet(models.Model):
    currency = models.TextField(max_length=3, choices=CURRENCY_LIST)
    amont = models.FloatField()
    owner = models.ManyToManyField(User)


class CategoryModel(models.Model):
    category_name = models.TextField()
    description = models.TextField()


class ExpenseModel(models.Model):
    amount_of_outcome = models.IntegerField()
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
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
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    cathegory = models.ForeignKey(
        CategoryModel, on_delete=models.SET_NULL, null=True)


class GoalModel(models.Model):
    goal_name = models.TextField
    description = models.TextField
    author = models.ForeignKey(User, on_delete=models.CASCADE)
