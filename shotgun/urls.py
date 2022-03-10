"""shotgun URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include
from shotgunapi.views import register_user, login_user
from rest_framework import routers
from shotgunapi.views.tag import TagView
from shotgunapi.views.scrapbook_tag import ScrapbookTagView
from shotgunapi.views.image import ImageView
from shotgunapi.views.scrapbook import ScrapbookView
from shotgunapi.views.app_users import AppUserView


router = routers.DefaultRouter(trailing_slash=False)

router.register(r'image', ImageView, 'image')

router.register(r'tags', TagView, 'tag')

router.register(r'appusers', AppUserView, 'appuser')

router.register(r'users', AppUserView, 'user')

router.register(r'scrapbooktags', ScrapbookTagView, 'scrapbooktags')

router.register(r'scrapbook', ScrapbookView, 'scrapbook')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('', include(router.urls))
   
]
