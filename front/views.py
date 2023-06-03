from django.contrib.auth import get_user_model, logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import get_object_or_404, redirect, render

from budget.models import Wallet, CategoryModel, IncomeModel, ExpenseModel

from .forms import ExpenseForm, IncomeForm, WalletForm

User = get_user_model()


def index_view(request):
    if request.user.is_authenticated:
        user = request.user
        user_name = user.first_name
        wallets = Wallet.objects.filter(owner=user)
        context = {
            "user_name": user_name,
            "wallets": wallets,
        }
        return render(request, 'user.html', context)
    else:
        return render(request, 'welcome.html')


def logout_view(request):
    logout(request)
    return render(request, 'logout.html')


def reg_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            # Перенаправление на главную страницу после регистрации
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Перенаправление на главную страницу после входа
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
# Кошелек


def wallet_view(request, pk):
    wallet = Wallet.objects.get(id=pk)
    incomes = IncomeModel.objects.filter(wallet=wallet).order_by('-date')[:5]
    expenses = ExpenseModel.objects.filter(wallet=wallet).order_by('-date')[:5]
    context = {'wallet': wallet,
               'incomes': incomes,
               'expenses': expenses}
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
    categories = CategoryModel.objects.all()
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
    return render(request, 'new_income.html', {'form': form,
                                               'wallet': wallet,
                                               'categories': categories})

# Expense


def new_expense(request, wallet_pk):
    wallet = Wallet.objects.get(id=wallet_pk)
    categories = CategoryModel.objects.all()
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
    return render(request, 'new_expense.html', {'form': form,
                                                'wallet': wallet,
                                                'categories': categories})
