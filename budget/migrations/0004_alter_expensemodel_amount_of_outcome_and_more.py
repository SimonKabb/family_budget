# Generated by Django 4.2.1 on 2023-05-31 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0003_alter_wallet_amont_alter_wallet_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensemodel',
            name='amount_of_outcome',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='incomemodel',
            name='amount_of_income',
            field=models.PositiveIntegerField(),
        ),
    ]
