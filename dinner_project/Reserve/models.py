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
