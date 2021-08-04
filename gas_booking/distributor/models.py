from userauth.models import User
from django.db import models




class AddGas(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gas_name = models.CharField(verbose_name="Gas Name", max_length=20, null=True)
    gas_number = models.IntegerField(verbose_name="Number of Gas", null=True)

    def __str__(self):
        return str(self.gas_name)