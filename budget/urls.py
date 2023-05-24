from django.urls import include, path
from rest_framework.routers import SimpleRouter

from budget.views import CategoryViewSet, UserViewSet, ExpenseViewSet

router = SimpleRouter()

router.register('category', CategoryViewSet)
router.register('users', UserViewSet)
router.register('expense', ExpenseViewSet)

urlpatterns = [
    path('api_v1/', include(router.urls)),
]
