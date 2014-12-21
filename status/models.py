from __future__ import unicode_literals
from django.db import models

# Create your models here.

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
