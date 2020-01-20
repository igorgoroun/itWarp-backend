from django.db import models
from django.utils.translation import gettext as _
from rest_framework import serializers


# Company model
class Company(models.Model):
    # hardcoded static values !moved to translate
    # code_short = 'ФОП'
    # code_full = 'Фізична особа-підприємець'
    code_short = _('FOP')
    code_full = _('Entrepreneur')

    # id = models.AutoField(primary_key=True)
    name_last = models.CharField(max_length=64)
    name_first = models.CharField(max_length=64)
    name_middle = models.CharField(max_length=64)
    address_line_1 = models.CharField(max_length=128)
    address_line_2 = models.CharField(max_length=128)
    address_line_3 = models.CharField(max_length=128)
    itn = models.CharField(max_length=16)
    reg = models.CharField(max_length=32)
    single_tax = models.BooleanField(default=True)

    def __str__(self):
        return self.fop_name_short()

    def __setattr__(self, key, value):
        if key in ['name_last', 'name_first', 'name_middle']:
            value = str(value).capitalize()
        super().__setattr__(key, value)

    def fop_name_full(self):
        return "{} {} {} {}".format(self.code_full, self.name_last, self.name_first, self.name_middle)

    def fop_name_short(self):
        return "{} {} {}. {}.".format(self.code_short, self.name_last, self.name_first[:1], self.name_middle[:1])

    def own_name_full(self):
        return "{} {} {}".format(self.name_last, self.name_first, self.name_middle)

    def own_name_short(self):
        return "{} {}. {}.".format(self.name_last, self.name_first[:1], self.name_middle[:1])

    def address(self):
        return "{} {} {}".format(self.address_line_1, self.address_line_2, self.address_line_3)


# Company Serializer
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name_last', 'name_first', 'name_middle',
                  'address',
                  'itn', 'reg', 'single_tax',
                  'code_short', 'code_full',
                  'fop_name_full', 'fop_name_short', 'own_name_full', 'own_name_short'
                  )
