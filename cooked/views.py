from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login
from .models import Meal, Kitchn
from .forms import KitchenForm

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



    