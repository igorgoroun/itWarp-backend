# Generated by Django 2.1.7 on 2019-04-19 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(max_length=32)),
                ('bank_number', models.CharField(max_length=6)),
                ('bank_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_last', models.CharField(max_length=64)),
                ('name_first', models.CharField(max_length=64)),
                ('name_middle', models.CharField(max_length=64)),
                ('address_line_1', models.CharField(max_length=128)),
                ('address_line_2', models.CharField(max_length=128)),
                ('address_line_3', models.CharField(max_length=128)),
                ('itn', models.CharField(max_length=16)),
                ('reg', models.CharField(max_length=32)),
                ('single_tax', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('address_line_1', models.CharField(max_length=128)),
                ('address_line_2', models.CharField(max_length=128)),
                ('address_line_3', models.CharField(max_length=128)),
                ('representative_name_last', models.CharField(max_length=64)),
                ('representative_name_first', models.CharField(max_length=64)),
                ('representative_name_middle', models.CharField(max_length=64)),
                ('representative_position', models.CharField(max_length=16)),
                ('itn', models.CharField(max_length=16)),
                ('reg', models.CharField(max_length=32)),
                ('single_tax', models.BooleanField(default=True)),
                ('is_fop', models.BooleanField(default=False)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partners', to='company.Company')),
            ],
        ),
        migrations.AddField(
            model_name='bankaccount',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bank_accounts', to='company.Company'),
        ),
        migrations.AddField(
            model_name='bankaccount',
            name='partner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bank_accounts', to='company.Partner'),
        ),
    ]