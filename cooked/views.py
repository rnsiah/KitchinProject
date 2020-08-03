from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .models import Meal, Kitchn
from .forms import KitchenForm, MealForm

def signupuser(request):
    if request.method=='GET':
        return render(request, 'cooked/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user=User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('home')
            except IntegrityError:
                 return render(request, 'cooked/signupuser.html', {'form':UserCreationForm(), 'error':'This username is already in use, please select a new username'})
        else:
             return render(request, 'cooked/signupuser.html', {'form':UserCreationForm(), 'error':'The passwords you entered do not match, please update passwords.'})
      

def kitchin(request):
    return render(request, 'cooked/kitchin.html')


def home(request):
    meals = Meal.objects.all()
    return render(request, 'cooked/home.html', context={'meals':meals})

def openkitchen(request):
    if request.method == 'GET': 
        return render(request, 'cooked/openkitchen.html', {'form':KitchenForm()})

    else:
        form = KitchenForm(data=request.POST)
        newKitchen = form.save(commit=False)
        newKitchen.user=request.user
        newKitchen.save()
        return redirect(to='home') 

    #return render(request, "cooked/openkitchen.html", {"form": form}) 

def view_meal(request, pk):
    meal = get_object_or_404(Meal, pk=pk) 
    

    return render(request, "cooked/meal_detail.html",

                  {"meal": meal})
def logoutuser(request):
    if request.method=='POST':
        logout(request)
        return redirect('kitchin')


def loginuser(request):
    if request.method=='GET':
        return render(request, 'cooked/loginuser.html', {'form':AuthenticationForm()})
    else:
        user= authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'cooked/loginuser.html', {'form':AuthenticationForm(), 'error':'Username and password do not match'})
        else:
            login(request, user)
            return redirect('home')
            


def createmeal(request):
    if request.method == 'GET': 
        return render(request, 'cooked/createmeal.html', {'form':MealForm()})

    else:
        form = MealForm(data=request.POST)
        newMeal = form.save(commit=False)
        newMeal.user=request.user
        newMeal.kitchen = get_kitchen_for_user(request)
        newMeal.save()
        return redirect(to='createmeal') 

    #return render(request, "cooked/openkitchen.html", {"form": form}) 


def all_kitchens(request):
    kitchens = Kitchn.objects.all()
    return render(request, 'cooked/allkitchens.html', context={'kitchens':kitchens})



def get_kitchen_for_user(request):
    """
    Get's kitchen for user
    """
 
    kitchen = Kitchn.objects.filter(user=request.user)[0]
    return kitchen
 