from django import forms
from .models import Profile,Restaurant,Image
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#create your forms here

class SignUpForm(UserCreationForm):
    '''
    A signup form that picks both user information and the profile information
    '''

    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    username=forms.CharField(max_length=30, required=False, help_text='Optional.')
    sex = forms.ChoiceField(choices=(('Male','Male'),('Female','Female')))
    profile_image=forms.ImageField()
    class Meta:
        model = User
        fields = ('first_name','last_name','email','username','profile_image','sex','password1', 'password2')
class RestaurantForm(forms.ModelForm):
    class Meta:
        model= Restaurant
        fields=('name','phone_number','Opening_Hours','Closing_Hours','email')
