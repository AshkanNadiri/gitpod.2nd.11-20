from django.db import models


# Create your models here.
class Branch(models.Model):
    branch = models.CharField(max_length = 30)
    branch_location = models.CharField(max_length = 30)

    def __str__(self):
        return f"Branch : {self.branch} | Location : {self.branch_location}"
