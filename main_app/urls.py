from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('consoles/', views.consoles_index, name='consoles_index'),
    path('genre/', views.about, name='genre'),
    path('title/', views.about, name='title'),
    path('blog/', views.about, name='blog'),
    path('accounts/signup/', views.signup, name='signup'),
]
