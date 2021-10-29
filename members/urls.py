from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
urlpatterns = [

	path('login_user/', login_user, name='login_user'),
	path('logout_user/', logout_user, name='logout_user'),
	path('register_user/', register_user, name='register_user'),
	path('password/', auth_views.PasswordChangeView.as_view()),
]