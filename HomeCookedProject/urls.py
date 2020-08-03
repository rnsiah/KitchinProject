"""HomeCookedProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from cooked import views as cooked_views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    #auth
    path('signup/', cooked_views.signupuser, name='signupuser'),


    path('home', cooked_views.home, name='home'),

    path('openkitchen', cooked_views.openkitchen, name='openkitchen'),

    path('cooked/<int:pk>/meal_detail/', cooked_views.view_meal, name='meal_detail'),

    # path('albums/<int:pk>/edit/', mymusic_views.edit_album, name='edit_album'),

    #path('viewmeals'), 

    #   path('albums/<int:pk>/', mymusic_views.view_album, name='view_album')

]
