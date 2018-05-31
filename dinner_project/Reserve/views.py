from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import SignUpForm,RestaurantForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth import login,authenticate
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
            return redirect(welcome)
            login(request,user)
            return redirect(welcome)
    else:
        form=SignUpForm()
    return render(request,'signup.html',{"form":form})
@login_required(login_url='/accounts/login')
def welcome(request):
    title="Welcome to reserve"
    profile=Profile.objects.get(user=request.user)
    return render(request,'Hotel/welcome.html',{"title":title,"profile":profile})
def hotel(request):
    title="Find the hotel near you"
    return render(request,'find.html',{"title":title})
def restaurant(request,profile_id):
    current_profile=Profile.objects.get(id=profile_id)
    return render (request,'rest.html',{"current_profile":current_profile})
def add(request,profile_id):
    current_profile=Profile.objects.get(id=profile_id)

    if request.method == 'POST':
        form=RestaurantForm(request.POST,request.FILES)
        if form.is_valid():
            rest_form=form.save(commit=False)
            rest_form.user=current_profile

    else:
            form=RestaurantForm()
    return render(request,'form1.html',{"form":form,"current_profile":current_profile})
