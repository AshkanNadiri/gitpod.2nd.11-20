from django.db import models
import uuid



# Create your models here.


class Branch(models.Model):

    branch_name = models.CharField(max_length = 30)
    branch_location = models.CharField(max_length = 30)
    location_id = str(uuid.uuid4())


    class Meta:
        verbose_name_plural = 'Branches'

    def __str__(self):
        return (f"Bank : {self.branch_name} | Location : {self.branch_location}")


class Customer(models.Model):
    customer_gender = (
        ('male','MALE'),
        ('female','FEMALE'),
        ('other','OTHER')
    )
    branch = models.ForeignKey(
        Branch,
        on_delete = models.CASCADE)
    customer_name = models.CharField(max_length = 30)
    customer_gender = models.CharField(
        max_length = 20,
        choices = customer_gender,
        default = customer_gender[0]
    )
    def __str__(self):
        return (f"Name: {self.customer_name}| Gender: {self.customer_gender}")


class Account(models.Model):
    customer = models.OneToOneField(
        Customer,
        on_delete = models.CASCADE)
    
    account_type = [
        ('debit','DEBIT'),
        ('credit','CREDIT'),
        ('checking','CHECKING'),
        ('saving','SAVING')
    ]

    amount = models.CharField(max_length =30)
    account_options = models.CharField(
        max_length = 30,
        choices = account_type,
        default = account_type[0]
    )
    def __str__(self):
        return (f"Customer: {self.customer.customer_name}| Account type: {self.account_options}| Amount: {self.amount}")


class Product(models.Model):
    account = models.ForeignKey(
        Account,
        on_delete = models.CASCADE
    )
    product_types = (
        ('mortgage','MORTGAGE'),
        ('loan','LOAN'),
        ('leasing','LEASING'),
        ('treasury','TREASURY'),
        ('ach','ACH')   
    )
    product_options = models.CharField(
        max_length = 30,
        choices = product_types,
        default = product_types[0]
    )

    def __str__ (self):
        return (f"{self.account} | Product: {self.product_options}")


