from django.db import models



# Create your models here.
class City(models.Model):
    city_name = models.CharField(max_length =20)

    class Meta:
        verbose_name_plural = 'cities'
    def __str__(self):
        return (f"City: {self.city_name}")

class Branch(models.Model):
    city = models.ForeignKey(City,on_delete = models.CASCADE)

    branch_name = models.CharField(max_length = 30,default='N/A')
    branch_location = models.CharField(max_length = 30,default='N/A')

    class Meta:
        verbose_name_plural = 'Branches'

    def __str__(self):
        return (f"Bank : {self.branch_name} | Location : {self.branch_location}| City: {self.city}")


class Customer(models.Model):
    customer_gender = (
        ('male','MALE'),
        ('female','FEMALE'),
        ('other','OTHER')
    )
    branch = models.ForeignKey(
        Branch,
        on_delete = models.CASCADE)
    customer_name = models.CharField(max_length = 30,default='N/A')
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

    amount = models.CharField(max_length =30,default='N/A')
    account_options = models.CharField(
        max_length = 30,
        choices = account_type,
        default = account_type[0]
    )
    def __str__(self):
        return (f"Customer: {self.customer.customer_name}| Account type: {self.account_options}| Amount: {self.amount}")


# class Product(models.Model):
#     account = models.OneToOneField(
#         Account,
#         on_delete = models.CASCADE
#     )
