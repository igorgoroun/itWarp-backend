from django.db import models
from .company import Company


class Partner(models.Model):
    company = models.ForeignKey(to=Company, related_name='partners', null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    address_line_1 = models.CharField(max_length=128)
    address_line_2 = models.CharField(max_length=128)
    address_line_3 = models.CharField(max_length=128)
    representative_name_last = models.CharField(max_length=64)
    representative_name_first = models.CharField(max_length=64)
    representative_name_middle = models.CharField(max_length=64)
    representative_position = models.CharField(max_length=16)
    itn = models.CharField(max_length=16)
    reg = models.CharField(max_length=32)
    single_tax = models.BooleanField(default=True)
    is_fop = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def __setattr__(self, key, value):
        if key in ['representative_name_last', 'representative_name_first', 'representative_name_middle']:
            value = str(value).capitalize()
        super().__setattr__(key, value)
