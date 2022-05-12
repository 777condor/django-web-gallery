from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('addpic/', views.addPicture, name='addpic'),
	path('picture/<str:pk>', views.viewPicture, name='viewpic')
]
