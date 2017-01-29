import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Synergy.settings")

import csv

from django.shortcuts import render
from .models import wattmodel

with open("data.csv") as f:
        reader = csv.reader(f)
        for row in reader:
                created = wattmodel()
                created.area=row[0],
                created.income=row[1],
                created.wattusage=row[2],
                created.save()

