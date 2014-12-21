# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Account(models.Model):
    id = models.CharField(primary_key=True, max_length=8)
    password = models.CharField(max_length=32)
    name = models.CharField(max_length=64)
    perm = models.CharField(max_length=8)
    senior = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'account'


class Clar(models.Model):
    clar_id = models.IntegerField(primary_key=True)
    team_id = models.CharField(max_length=8)
    category = models.CharField(max_length=32)
    content = models.TextField()
    response = models.TextField()
    public = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'clar'


class Login(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    team_id = models.CharField(max_length=8)
    success = models.IntegerField()
    ip = models.CharField(db_column='IP', max_length=32)  # Field name made lowercase.
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'login'


class Problemset(models.Model):
    pid = models.CharField(primary_key=True, max_length=8)
    score = models.IntegerField()
    title = models.CharField(max_length=255)
    differ = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'problemset'


class Status(models.Model):
    run_id = models.IntegerField(primary_key=True)
    team_id = models.CharField(max_length=8)
    pid = models.CharField(max_length=8)
    result = models.CharField(max_length=64)
    time = models.DateTimeField()
    ip = models.CharField(max_length=64)
    output = models.CharField(max_length=255)
    solution = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'status'
