from django.urls import path

from .views import (new_wallet, new_income, index_view,
                    wallet_view, delete_wallet,
                    new_expense, logout_view, reg_view, login_view)

urlpatterns = [
    path('wallet/<pk>/', wallet_view, name='wallet'),
    path('', index_view, name='index'),
    path('new_wallet', new_wallet, name='new_wallet'),
    path('delete_wallet/<wallet_pk>/', delete_wallet, name='delete_wallet'),
    path('new_income/<int:wallet_pk>/', new_income, name='new_income'),
    path('new_expense/<int:wallet_pk>/', new_expense, name='new_expense'),
    path('logout/', logout_view, name='logout'),
    path('login', login_view, name='login'),
    path('registration', reg_view, name='registration'),
]
