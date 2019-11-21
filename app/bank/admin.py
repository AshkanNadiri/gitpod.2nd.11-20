from __future__ import unicode_literals

from django.contrib import admin
from .models import Branch, Customer, Account


admin.site.register((
    Branch,
    Customer,
    Account,
    ))
