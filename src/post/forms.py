from django import forms
# from tinymce import TinyMCE
from django.forms import ModelForm
from tinymce.widgets import TinyMCE
from .models import Post, Comment
from allauth.account.forms import SignupForm
from django import forms



class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCE(
            attrs={'required': True, 'cols': 30, 'rows': 10}
        )
    )

    class Meta:
        model = Post
        fields = ('title', 'overview', 'content','thumbnail', 
        'category', 'previous_post', 'next_post','featured' )


class CommentForm(forms.ModelForm):

    content =forms.CharField(label='Laissez votre commentaire' ,widget=TinyMCE(attrs={
         'class'       : 'form-control',
         'placeholder' : 'Laissez votre commentaire',
         'id'          : 'usercomment',
         'rows'        : '4',
        }))

    class Meta:
        model = Comment
        fields = ('content',)





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
