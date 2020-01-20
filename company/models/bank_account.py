from django.db import models
from .company import *
from .partner import *


class BankAccount(models.Model):
    account_number = models.CharField(max_length=32, default=None)
    iban = models.CharField(max_length=64, default=None)
    bank_number = models.CharField(max_length=6)
    bank_name = models.CharField(max_length=64)
    company = models.ForeignKey(to=Company, related_name='bank_accounts', null=True, on_delete=models.CASCADE)
    partner = models.ForeignKey(to=Partner, related_name='bank_accounts', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "{}, {}".format(self.account_number, self.bank_name)
