from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm, LoginForm

# FORMULAIRE DE CONNECTION
class LoginForm(AuthenticationForm):
	username = forms.CharField(label="Nom d'utilisateur", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':"Nom d'utilisateur"}))
	password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':"Mot de passe"}))


# FORMULAIRE D'INSCRIPTION
class RegisterUserForm(UserCreationForm):
	username  = forms.CharField(label="Nom d'utilisateur", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':"Nom d'utilisateur"}))
	email     = forms.CharField(label="Email", widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':"Adresse Email"}))
	password1 = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':"Mot de passe"}))
	password2 = forms.CharField(label="Confirmer mot de passe", widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':"Confirmer votre mot de passe"}))

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')


class CustomSignupForm(SignupForm):
    username  = forms.CharField(max_length=30, label="Nom d'utilisateur", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Nom d'utilisateur"}))
    email     = forms.CharField(max_length=30, label='Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password1 = forms.CharField(label='Mot de passe', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder' : 'Mot de passe', 'type': 'password', 'name': 'password1', 'id':'id_password1'}))
    password2 = forms.CharField(label='Confirmer mot de passe', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder' : 'Confimer mot de passe', 'type': 'password', 'name': 'password2', 'id':'id_password2'}))

    def save(self, request):
        user           = super(CustomSignupForm, self).save(request)
        user.username  = self.cleaned_data['username']
        user.email     = self.cleaned_data['email']
        user.password1 = self.cleaned_data['password1']
        user.password2 = self.cleaned_data['password2']
        user.save()
        return user



class MyLoginForm(LoginForm):
    username  = forms.CharField(max_length=30, label="Nom d'utilisateur", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Nom d'utilisateur"}))
    password  = forms.CharField(label='Mot de passe', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder' : 'Mot de passe', 'type': 'password', 'name': 'password1', 'id':'id_password1'}))


    def login(self, *args, **kwargs):

        # Add your own processing here.

        # You must return the original result.
        return super(MyLoginForm, self).login(*args, **kwargs)