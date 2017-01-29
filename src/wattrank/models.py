from django.db import models

class wattmodel(models.Model):
    area = models.CharField(max_length=50)
    income = models.CharField(max_length=50)
    wattusage = models.CharField(max_length=50)
