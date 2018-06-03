from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import SignUpForm,RestaurantForm,ImageForm,MenuForm,MakeForm,FoodForm
from django.contrib.auth.decorators import login_required
from .models import Profile,Restaurant,Image,Menu,Customer
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User

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
    current_profile=Profile.objects.get(id=request.user.id)
    return render(request,'find.html',{"title":title,"current_profile":current_profile})
def restaurant(request,profile_id):
    current_profile=Profile.objects.get(id=profile_id)
    restaurant_info=Restaurant.objects.filter(id=profile_id)
    images=Image.objects.filter(restaurant=restaurant_info)
    menus=Menu.objects.filter(restaurant=restaurant_info)
    requests=Customer.objects.filter(restaurant=restaurant_info)
    return render (request,'rest.html',{"current_profile":current_profile,"restaurant_info":restaurant_info,"images":images,"menus":menus,"requests":requests})
def add(request,profile_id):
    current_profile=Profile.objects.get(id=profile_id)

    if request.method == 'POST':
        form=RestaurantForm(request.POST,request.FILES)
        if form.is_valid():
            rest_form=form.save(commit=False)
            rest_form.user=current_profile
            rest_form.save()
            return redirect(restaurant,current_profile.id )
    else:
            form=RestaurantForm()
    return render(request,'form1.html',{"form":form,"current_profile":current_profile})
def image(request,profile_id):
    current_profile=Restaurant.objects.get(id=profile_id)

    if request.method == 'POST':
        form=ImageForm(request.POST,request.FILES)
        if form.is_valid():
            image_form=form.save(commit=False)
            image_form.restaurant=current_profile
            image_form.save()
            return redirect(restaurant,current_profile.id )
    else:
        form=ImageForm()
    return render (request,'image.html',{"form":form,"current_profile":current_profile})
def menu(request,profile_id):
    current_profile=Restaurant.objects.get(id=profile_id)

    if request.method == 'POST':
        form=MenuForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(restaurant,current_profile.id )
    else:
        form=MenuForm()
    return render (request, 'menu.html',{"form":form,"current_profile":current_profile})
def customer(request,profile_id):
    current_profile=Profile.objects.get(id=profile_id)
    title="welcome customer"
    rests=Customer.objects.filter(name=current_profile)
    return render(request,'customer.html',{"title":title,"current_profile":current_profile,"rests":rests})
def make(request,profile_id):
    current_profile=Profile.objects.get(id=profile_id)

    if request.method == 'POST':
        form=MakeForm(request.POST)
        if form.is_valid():
            make_form=form.save(commit=False)
            make_form.name=current_profile
            make_form.save()
            return redirect(customer,current_profile.id )
    else:
        form=MakeForm()
    return render (request, 'make.html',{"form":form,"current_profile":current_profile})
def moreinfo(request,profile_id):
    current_profile=Profile.objects.get(id=profile_id)
    restaurant_info=Restaurant.objects.filter(id=profile_id)
    images=Image.objects.filter(restaurant=restaurant_info)
    menus=Menu.objects.filter(restaurant=restaurant_info)
    return render (request,'info.html',{"current_profile":current_profile,"restaurant_info":restaurant_info,"images":images,"menus":menus})
def food(request):
    current_profile=Profile.objects.get(id=request.user.id)
    current_customer=Customer.objects.get(id=request.user.id)
    if request.method == 'POST':
        form=FoodForm(request.POST,instance=current_customer)
        if form.is_valid():
            food=form.save(commit=False)

            return redirect(customer,current_profile.id )
    else:
        form=FoodForm()
    return render (request,'food.html',{"current_profile":current_profile,"form":form})
def direction(request):
    title="directions"
    current_profile=Profile.objects.get(id=request.user.id)
    return render(request,'direct.html',{"title":title,"current_profile":current_profile})
