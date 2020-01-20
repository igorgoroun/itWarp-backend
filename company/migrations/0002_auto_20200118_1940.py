# Generated by Django 3.0.2 on 2020-01-18 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankaccount',
            name='iban',
            field=models.CharField(default=None, max_length=64),
        ),
        migrations.AlterField(
            model_name='bankaccount',
            name='account_number',
            field=models.CharField(default=None, max_length=32),
        ),
    ]