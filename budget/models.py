from django.contrib.auth import get_user_model
from django.db import models
import datetime
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
    name = models.TextField(max_length=64)
    currency = models.TextField(max_length=3, choices=CURRENCY_LIST)
    amont = models.FloatField(default=0)
    owner = models.ManyToManyField(User)

    class Meta:
        verbose_name = 'Кошелек'
        verbose_name_plural = 'Кошельки'

    def __str__(self):
        return self.name


class CategoryModel(models.Model):
    category_name = models.TextField()
    description = models.TextField()

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.category_name


class ExpenseModel(models.Model):
    amount_of_outcome = models.PositiveIntegerField()
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    cathegory = models.ForeignKey(
        CategoryModel, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        outcome = '-' + str(self.amount_of_outcome) + '. Дата: ' + \
            str(self.date.date().isoformat()) + '. Время: ' + \
            str(self.date.time().strftime("%H:%M:%S"))
        return outcome


class IncomeModel(models.Model):
    amount_of_income = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    cathegory = models.ForeignKey(
        CategoryModel, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        outcome = str(self.amount_of_income) + '. Дата: ' + \
            str(self.date.date().isoformat()) + '. Время: ' + \
            str(self.date.time().strftime("%H:%M:%S"))
        return outcome


class GoalModel(models.Model):
    goal_name = models.TextField
    description = models.TextField
    author = models.ForeignKey(User, on_delete=models.CASCADE)
