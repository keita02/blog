from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
	# first_name = forms.CharField(max_length=50)
	# last_name = forms.CharField(max_length=50)


	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(RegisterUserForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs['placeholder'] = "Nom d'utilisateur"
		self.fields['email'].widget.attrs['placeholder'] = "Adresse Email"
		self.fields['password1'].widget.attrs['placeholder'] = "Mot de passe"
		self.fields['password2'].widget.attrs['placeholder'] = "Confirmer mot de passe"

		for field in self.fields:
		    self.fields[field].widget.attrs['class'] = 'form-control'

	# class Meta:
	# 	model = User
	# 	fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

