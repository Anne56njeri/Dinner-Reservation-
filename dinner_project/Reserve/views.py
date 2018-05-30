from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from .models import Profile
# Create your views here.
def signup(request):
    '''
    when the user saves the form this function is called and saves both to the user and profile model
    '''
    if request.method == 'POST':
        form=SignUpForm(request.POST,request.FILES)
        if form.is_valid():
            user=form.save()
            user.refresh_from_db()
            user.profile.username=form.cleaned_data.get('username')
            user.profile.profile_image=form.cleaned_data.get('profile_image')
            user.profile.sex=form.cleaned_data.get('sex')
            user.save()
            raw_password=form.cleaned_data.get('password1')
            user=authenticate(username=user.username,password=raw_password)
    else:
        form=SignUpForm()
    return render(request,'signup.html',{"form":form})

def welcome(request):
    title="Welcome to reserve"
    return render(request,'Hotel/welcome.html',{"title":title})
