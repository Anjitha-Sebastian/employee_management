from django.contrib import admin
from django.urls import path,include
from employee import views

# urlpatterns = [
    # path('index',views.index),
    # path('index',views.login),
    # path('index',views.register)
# ]
urlpatterns = [
    path('index',views.IndexView.as_view()),
    path('login',views.LoginView.as_view()),
    path('register',views.RegistrationView.as_view())

]