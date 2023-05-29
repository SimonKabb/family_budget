from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import CategoryModel, ExpenseModel, GoalModel, IncomeModel, Wallet
from .serializers import (CategorySerializer, ExpenseSerializer,
                          GoalSerializer, IncomeSerializer, UserSerializer, WalletSerializer)

User = get_user_model()


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer


class ExpenseViewSet(viewsets.ModelViewSet):
    def create(self, request):
        amount = request.data.get('amount_of_outcome')
        user = request.user
        user.wallet_balance -= amount
        user.save()
        ExpenseModel.objects.create(
            amount_of_outcome=amount,
            description=request.data.get('description'),
            author=user)
        return Response({'message': 'Expense created successfully'})
    queryset = ExpenseModel.objects.all()
    serializer_class = ExpenseSerializer


class IncomeViewSet(viewsets.ModelViewSet):
    def create(self, request):
        amount = request.data.get('amount_of_income')
        wallet = Wallet.objects.get(id=request.data.get('wallet'))
        print(wallet.amont)
        wallet.amont += amount
        wallet.save()
        IncomeModel.objects.create(
            amount_of_income=amount,
            description=request.data.get('description'),
            author=request.user,
            wallet=Wallet.objects.get(id=request.data.get('wallet')))
        return Response({'message': 'Income created successfully'})
    queryset = IncomeModel.objects.all()
    serializer_class = IncomeSerializer


class GoalViewSet(viewsets.ModelViewSet):
    queryset = GoalModel.objects.all()
    serializer_class = GoalSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
