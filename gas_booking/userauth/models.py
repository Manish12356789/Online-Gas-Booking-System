from django.db import models
from django.contrib.auth.models import User, UserManager
from django_countries.fields import CountryField
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

# User = settings.AUTH_USER_MODEL    

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

# from django.contrib.auth.models import User, UserManager

class Consumer(models.Model): # for consumer 
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='consumer')
    mobile_phone = models.CharField(unique = True, null=True, max_length=10, help_text="Enter Your mobile number without country code.")
    address = models.CharField(max_length=1024, null=True, help_text="Your street name and house number.")
    zip_code = models.CharField( max_length=12, null=True)
    city = models.CharField(max_length=1024, null=True)
    state = models.CharField(max_length=1024, null=True)
    country = CountryField(blank=True, null=True)
    date_of_birth = models.DateField(null=True)
    additional_information = models.CharField(verbose_name=("Additional information"), max_length=4096, null=True)

    objects = UserManager()

    def __str__(self):
         return str(self.user.first_name + " " + self.user.last_name)

    # @receiver(post_save, sender=User)
    # def update_profile_signal(sender, instance, created, **kwargs):
    #     if created:
    #         Consumer.objects.create(user=instance)
    #     instance.consumer.save()


class Distributor(models.Model):  #for distributor
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='distributor')
    distributor_name = models.CharField(max_length=1024, null=True, help_text="Your store name." )
    mobile_phone = models.CharField(max_length=10, help_text="Enter Your mobile number without country code.")
    address = models.CharField(max_length=1024, null=True, help_text="Your street name and house number.")
    zip_code = models.CharField( max_length=12, null=True)
    city = models.CharField(max_length=1024, null=True)
    state = models.CharField(max_length=1024, null=True)
    country = CountryField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    website = models.URLField(blank=True, null=True, verbose_name="Website", help_text="Your stores website url if you have.")
    proof_pic = models.ImageField(null=True, blank=True, verbose_name="Pan Card ", help_text="Your Id proof must have pan card.")
    additional_information = models.CharField(verbose_name=("Additional information"), max_length=4096, null=True)

    objects = UserManager()

    def __str__(self):
        return str(self.distributor_name)

    # @receiver(post_save, sender=User)
    # def update_profile_signal(sender, instance, created, **kwargs):
    #     if created:
    #         Distributor.objects.create(user=instance)
    #     instance.distributor.save()




# class MyAccountManager(BaseUserManager):
#     def create_user(self, email, address,distributor_name, proof_pic, mobile_phone, password=None):
#         if not email:
#             raise ValueError('Users must have an email address')
#         if not address:
#             raise ValueError('Must have your address.')
#         if not mobile_phone:
#             raise ValueError('Enter your active phone number.')
#         if not distributor_name:
#             raise ValueError('Enter your active phone number.')
#         if not proof_pic:
#             raise ValueError('Enter your active phone number.')

#         user = self.model(
#             email=self.normalize_email(email),
#             password = password,
#             address = address,
#             mobile_phone = mobile_phone,
#             distributor_name=distributor_name,
#             proof_pic = proof_pic
#             )
#         user.password = make_password(password)
#         user.save(using=self._db)
#         return user


#     def create_superuser(self, email, mobile_phone, address, password=None):
#         user = self.create_user(
#             email=self.normalize_email(email),
#             password=password,
#             mobile_phone= mobile_phone,
#             address=address
#         )
#         user.is_admin = True
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user


# class UserDetails(AbstractBaseUser):
#     email = models.EmailField(verbose_name="email", max_length=60, unique=True)
#     distributor_name = models.CharField(max_length=1024, null=True, help_text="Your store name." )
#     # password = models.CharField(max_length=20)
#     date_joined	= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
#     last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
#     is_admin = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#     first_name = models.CharField(max_length=1024, blank=True, null=True)
#     last_name = models.CharField(max_length=1024, blank=True, null=True)

#     date_of_birth = models.DateField(blank=True, null=True)
#     address = models.CharField(max_length=1024, null=True, help_text="Your street name and house number.")
#     zip_code = models.CharField( max_length=12, null=True)
#     city = models.CharField(max_length=1024, null=True)
#     state = models.CharField(max_length=1024, null=True)
#     country = CountryField(blank=True, null=True)
#     #validators=[phone_regex], phone_regex = RegexValidator(regex=r"^\+(?:[0-9]●?){6,14}[0-9]$", message=("Enter a valid international mobile phone number starting with +(country code)"))
#     mobile_phone = models.CharField(verbose_name=("Mobile phone"), unique=True, max_length=10, help_text="Enter Your mobile number without country code.")
#     website = models.URLField(blank=True, null=True, verbose_name="Website", help_text="Your stores website url if you have.")
#     proof_pic = models.ImageField(null=True, verbose_name="Pan Card ", help_text="Your Id proof must have pan card.")
#     additional_information = models.CharField(verbose_name=("Additional information"), max_length=4096, null=True)


#     USERNAME_FIELD = 'mobile_phone'
#     REQUIRED_FIELDS = ['address','email', 'distributor_name', 'proof_pic']

#     objects = MyAccountManager()

#     def __str__(self):
#         return self.email

#     # For checking permissions. to keep it simple all admin have ALL permissons
#     def has_perm(self, perm, obj=None):
#         return self.is_admin

#     # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
#     def has_module_perms(self, app_label):
#         return True

