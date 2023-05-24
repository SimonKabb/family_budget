
from rest_framework import serializers

from .models import CategoryModel, ExpenseModel, GoalModel, IncomeModel, UserModel


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
        model = UserModel
        fields = '__all__'
