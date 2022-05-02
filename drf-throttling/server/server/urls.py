"""server URL Configuration

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
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from throttling import views as thv
from rest_framework.authtoken.views import obtain_auth_token
from scoperatethrottle2 import views as sctv

router=DefaultRouter()

router.register('noteapi',thv.NoteViewSet,basename='notepi')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),
    path('gettoken/',obtain_auth_token),
    path('getpost/',sctv.PostList.as_view()),
    path('retrievepost/<int:pk>/',sctv.PostRetreieve.as_view()),
    path('createpost/',sctv.PostCreate.as_view()),
    path('updatepost/<int:pk>/',sctv.PostUpdate.as_view()),
    path('deletepost/<int:pk>/',sctv.PostDestroy.as_view()),
]
