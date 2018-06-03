from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
# Create your models here.
class Profile(models.Model):
    '''
    We create a profile model to save the user profile information as they signup by the
    use of signals
    '''
    username=models.CharField(max_length=40)
    profile_image=models.ImageField(upload_to='profiles/')
    choices=(('Male','Male'),('Female','Female'))
    sex=models.CharField(_('sex'),max_length=30,blank=True,choices=choices)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()
    def __str__(self):
        return self.username
class Restaurant(models.Model):
    '''
    a model that allows Restaurant to register their business
    '''
    name=models.CharField(max_length=40)
    phone_number=models.CharField(max_length=40)
    email=models.EmailField(max_length=40)
    Opening_Hours=models.CharField(max_length=40)
    Closing_Hours=models.CharField(max_length=40)
    user=models.ForeignKey(Profile,null=True)
    def __str__(self):
        return self.name
class  Image(models.Model):
    image_path=models.ImageField(upload_to='images/',blank=True)
    description=models.CharField(max_length=40)
    restaurant=models.ForeignKey(Restaurant,null=True)
class Menu(models.Model):
    '''
    A model that stores information on the menu available
    '''

    food_name=models.CharField(max_length=40)
    food_image=models.ImageField(upload_to='images/',blank=True)
    price=models.CharField(max_length=40,null=True)
    restaurant=models.ForeignKey(Restaurant,null=True)
class Customer(models.Model):
    '''
    A model that saves customer information
    '''
    phone_number=models.IntegerField(max_length=40)
    restaurant=models.ForeignKey(Restaurant,null=True)
    choices=(('Cash','Cash'),('M-pesa','M-pesa'),('Credit_card','Credit_card'),('Debit_card','Debit_card'))
    Payment_method=models.CharField(_('Payment_method'),max_length=30,blank=True,choices=choices)
    Number_of_seats=models.CharField(max_length=40,null=True)
    
