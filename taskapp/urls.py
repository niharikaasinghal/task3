from django.urls import path 
from . import views

urlpatterns=[
    path('', views.index, name='index'), 
    path('login',views.login, name='login'),
    path('register',views.register , name='register'),
    path('write',views.write1,name='write'),
    path('blogs',views.blogs ,name='blogs'),
    path('post/<str:pk>',views.post,name='post'),
    path('doctors', views.list ,name='doctors'),
    path('book', views.book ,name='book'),
]