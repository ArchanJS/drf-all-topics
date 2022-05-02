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
from apis import views as v
from classbasedapis import views as vc
from genericapi import views as vg
from concreteapis import views as vcon
from viewsets import views as vsv
from vsmodels import views as vmv
from rest_framework.routers import DefaultRouter

# Creating router
router=DefaultRouter()

router.register('teacherapi',vsv.TeacherViewsets,basename='teacherapis')
router.register('itemapi',vmv.ItemViewwset,basename="itemapis")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('createpost',v.create_post),
    path('getallposts',v.get_all_posts),
    path('getapost/<int:id>',v.get_a_post),
    path('updatepostput/<int:id>',v.update_a_post_put),
    path('updatepostpatch/<int:id>',v.update_a_post_patch),
    path('deletepost/<int:id>',v.delete_a_post),
    path('note',vc.NoteAPIs.as_view()),
    path('note/<int:id>',vc.NoteAPIs.as_view()),
    path('comment',vg.CommentList.as_view()),
    path('createcomment',vg.CommentCreate.as_view()),
    path('retrievecomment/<int:pk>',vg.CommentRetrieve.as_view()),
    path('updatecomment/<int:pk>',vg.CommentUpdate.as_view()),
    path('deletecomment/<int:pk>',vg.CommentDestroy.as_view()),
    path('getallstudents',vcon.StudentList.as_view()),
    path('createstudent',vcon.StudentCreate.as_view()),
    path('retrievestudent/<int:pk>',vcon.StudentRetrieve.as_view()),
    path('updatestudent/<int:pk>',vcon.StudentUpdate.as_view()),
    path('destroystudent/<int:pk>',vcon.StudentDestroy.as_view()),
    path('studentlistcreate',vcon.StudentListCreate.as_view()),
    path('studentretrieveupdatedestroy/<int:pk>',vcon.StudentRetrieveUpdateDestroy.as_view()),
    path('',include(router.urls))
]
