from django import forms

from budget.models import Wallet


class WalletForm(forms.ModelForm):
    class Meta:
        model = Wallet
        fields = ('name', 'currency', 'amont')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(WalletForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(WalletForm, self).save(commit=False)
        if commit:
            instance.save()
            # Добавляем связь с владельцем кошелька
            instance.owner.add(self.user)
        return instance

    def clean_subject(self):
        data = self.cleaned_data['subject']
        return data
