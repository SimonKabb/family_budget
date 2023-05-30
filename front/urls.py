from django.urls import path
from .views import wallet_view, index_view

urlpatterns = [
    path('wallet/<pk>/', wallet_view, name='wallet'),
    path('', index_view, name='index')
]
