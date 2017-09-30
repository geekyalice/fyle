from __future__ import unicode_literals

from django.db import models
from rest_framework import serializers

# Create your models here.


class Banks(models.Model):
    name = models.CharField(max_length=49, blank=True, null=True)
    id = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'banks'


class Branches(models.Model):
    ifsc = models.CharField(primary_key=True, max_length=11)
    bank = models.ForeignKey(Banks, models.DO_NOTHING, blank=True, null=True)
    branch = models.CharField(max_length=74, blank=True, null=True)
    address = models.CharField(max_length=195, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=26, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'branches'


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        models = Banks
        fields = ('name',)


class BranchSerialzer(serializers.ModelSerializer):
    bank = BankSerializer()

    class Meta:
        model = Branches
        exclude = ('bank',)
        #fields = ('ifsc', 'branch', 'address', 'city', 'district', 'state')


