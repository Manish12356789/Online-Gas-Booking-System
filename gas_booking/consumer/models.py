from distributor.models import AddGas
from django.shortcuts import redirect
from django.db import models
from userauth.models import User, Distributor

from django.db.models.signals import post_save
from django.dispatch import receiver


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="order_details")
    order_date = models.DateField(null=True, auto_now_add=True)
    order_time = models.TimeField(null=True, auto_now_add=True)
    payable_amount = models.IntegerField( null=True, default=1500)
    status = models.CharField(max_length=50, default="pending")
    store_name = models.ForeignKey(Distributor, on_delete=models.CASCADE, null=True, related_name='store_name')
    gas_name = models.ForeignKey(AddGas, on_delete=models.CASCADE, null=True, related_name='name_of_gas')

    
    def __str__(self):
        # return str(self.user.first_name + " " + self.user.last_name)
        return str(self.store_name)

    class Meta:
        verbose_name = "Order"


class FeedbackComplaint(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="feedback_complaint")
    type = models.CharField(default="feedback", max_length=50)
    subject = models.CharField(null=True, max_length=50)
    message = models.CharField(null=True, max_length=1024)

    def __str__(self):
        return str(self.user.first_name +" " + self.user.last_name)


# @receiver(post_save, sender=UserDetails)
# def create_order(sender, instance, created, raw=False, **kwargs):
#     if created and not raw:
#         FeedbackComplaint.objects.create(user=instance)
#         print('Profile Created')

