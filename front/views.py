from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render, get_object_or_404

from budget.models import Wallet

from .forms import WalletForm, IncomeForm, ExpenseForm

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


# Кошелек
def wallet_view(request, pk):
    wallet = Wallet.objects.get(id=pk)
    context = {'wallet': wallet}
    return render(request, 'wallet.html', context)


def new_wallet(request):
    if request.method == 'POST':
        form = WalletForm(request.POST, user=request.user)
        if form.is_valid():
            name = form.cleaned_data['name']
            currency = form.cleaned_data['currency']
            amont = form.cleaned_data['amont']
            form.fields['name'].widget.attrs.update(
                {'class': 'form-control', 'style': 'height: 50px;'})
            form.fields['currency'].widget.attrs.update(
                {'class': 'form-control'})
            form.fields['amont'].widget.attrs.update({'class': 'form-control'})
            form.save()
            return redirect('/')
        return render(request, 'new_wallet.html', {'form': form})
    form = WalletForm()
    form.fields['name'].widget.attrs.update(
        {'class': 'form-control', 'style': 'height: 50px;'})
    form.fields['currency'].widget.attrs.update({'class': 'form-control'})
    form.fields['amont'].widget.attrs.update({'class': 'form-control'})
    return render(request, 'new_wallet.html', {'form': form})


def delete_wallet(request, wallet_pk):
    wallet = get_object_or_404(Wallet, pk=wallet_pk, owner=request.user)
    if request.method == 'POST':
        wallet.delete()
        return redirect('/')
    context = {'wallet': wallet}
    return render(request, 'delete_wallet.html', context)


# Income
def new_income(request, wallet_pk):
    wallet = Wallet.objects.get(id=wallet_pk)
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.author = request.user
            income.wallet = wallet
            income.save()
            wallet.amont += income.amount_of_income
            wallet.save()
            return redirect('wallet', pk=wallet.pk)
    else:
        form = IncomeForm(initial={'wallet': wallet})
    return render(request, 'new_income.html', {'form': form, 'wallet': wallet})

# Expense


def new_expense(request, wallet_pk):
    wallet = Wallet.objects.get(id=wallet_pk)
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.author = request.user
            expense.wallet = wallet
            expense.save()
            wallet.amont -= expense.amount_of_outcome
            wallet.save()
            return redirect('wallet', pk=wallet_pk)
    else:
        form = ExpenseForm(initial={'wallet': wallet})
    return render(request, 'new_expense.html', {'form': form, 'wallet': wallet})
