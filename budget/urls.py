from django.urls import include, path
from rest_framework.routers import SimpleRouter
from rest_framework_swagger.views import get_swagger_view

from budget.views import (CategoryViewSet, ExpenseViewSet, IncomeViewSet,
                          UserViewSet, WalletViewSet)

router = SimpleRouter()
schema_view = get_swagger_view(title='API Documentation')

router.register('category', CategoryViewSet)
router.register('users', UserViewSet)
router.register('expense', ExpenseViewSet)
router.register('income', IncomeViewSet)
router.register('wallet', WalletViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('docs', schema_view),
]
