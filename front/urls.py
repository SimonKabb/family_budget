from django.urls import path

from .views import new_wallet, index_view, wallet_view, delete_wallet

urlpatterns = [
    path('wallet/<pk>/', wallet_view, name='wallet'),
    path('', index_view, name='index'),
    path('new_wallet', new_wallet, name='new_wallet'),
    path('delete_wallet/<wallet_pk>/', delete_wallet, name='delete_wallet')
]
