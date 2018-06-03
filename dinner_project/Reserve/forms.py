from django import forms
from .models import Profile,Restaurant,Image,Menu,Customer
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
    '''
    A restaurant form that picks the restaurant information
    '''
    class Meta:
        model= Restaurant
        fields=('name','phone_number','Opening_Hours','Closing_Hours','email')
class ImageForm(forms.ModelForm):
    '''
    A form that picks the form about the restaurant
    '''
    class Meta:
        model=Image
        fields=('image_path','description')
class MenuForm(forms.ModelForm):
    '''
    A form that picks the food on the menu
    '''
    class Meta:
        model=Menu
        fields=('food_name','food_image','price','restaurant')
class MakeForm(forms.ModelForm):
    '''
    a form that saves the customers information when they make a reservation
    '''
    class Meta:
        model=Customer
        fields=('phone_number','Payment_method','Number_of_seats','restaurant')
class FoodForm(forms.ModelForm):
    '''
    A form that saves the food the customer has ordered
    '''
    class Meta:
        model=Customer
        fields=('food',)
