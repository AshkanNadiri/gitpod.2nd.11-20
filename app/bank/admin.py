from __future__ import unicode_literals

from django.contrib import admin
from .models import City, Branch, Customer, Account


admin.site.register((
    City,
    Branch,
    Customer,
    Account,
    # Product
    ))

