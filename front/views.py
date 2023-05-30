from budget.models import Wallet
from django.shortcuts import render
from django.contrib.auth import get_user_model
User = get_user_model()


def index_view(request):
    user = request.user
    print(user)
    user_name = user.first_name
    wallets = Wallet.objects.filter(owner=user)
    print(wallets)
    context = {
        "user_name": user_name,
        "wallets": wallets,
    }
    return render(request, 'user.html', context)


def wallet_view(request, pk):
    wallet = Wallet.objects.get(id=pk)
    context = {'wallet': wallet}
    return render(request, 'wallet.html', context)
