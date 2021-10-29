from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
# Create your views here.


def register_user(request):

	if request.method == 'POST':
		form = RegisterUserForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)

			login(request, user)
			messages.success(request, "Votre compte a été crée avec succès")
			return redirect('login_user')
	else:
		form = RegisterUserForm()

	context = {'form': form}

	return render(request, 'authenticate/register.html', context)





def login_user(request):

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.error(request, 'Identifiant ou mot de passe incorrect')
			return redirect('login_user')


	else:
		return render(request, 'authenticate/login.html')



@login_required(login_url='login_user')
def logout_user(request):
	logout(request)
	messages.success(request, 'Merci de votre temps sur notre blog')
	return redirect('login_user')