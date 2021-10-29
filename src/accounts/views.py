from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm, CustomSignupForm
from post.models import Author
from django.contrib import messages
# Create your views here.

class AccountSignupView(CustomSignupForm):
	pass

def register(request):

	if request.user.is_authenticated:
		return redirect('home')

	if request.method == 'POST':
		form = RegisterUserForm(request.POST)

		if form.is_valid():
			form.save()

			messages.success(request, 'Compte crée avec succès')
			return redirect('accounts:login')


	else:
		form = RegisterUserForm() 

	context = {'form':form}
	return render(request, 'accounts/register.html', context)