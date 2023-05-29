
from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import CategoryModel, ExpenseModel, GoalModel, IncomeModel, Wallet

User = get_user_model()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseModel
        fields = '__all__'


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeModel
        fields = '__all__'


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoalModel
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = '__all__'
