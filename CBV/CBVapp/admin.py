from django.contrib import admin
from CBVapp.models import Company, Products  # import from your app's models.py

admin.site.register(Company)
admin.site.register(Products)