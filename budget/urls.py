from django.urls import include, path
from rest_framework.routers import SimpleRouter

from budget.views import (CategoryViewSet, UserViewSet,
                          ExpenseViewSet, IncomeViewSet, WalletViewSet)

router = SimpleRouter()

router.register('category', CategoryViewSet)
router.register('users', UserViewSet)
router.register('expense', ExpenseViewSet)
router.register('income', IncomeViewSet)
router.register('wallet', WalletViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
