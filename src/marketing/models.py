from django.db import models

# Create your models here.
class SignUp(models.Model):
	email = models.EmailField()
	timestamp = models.DateTimeField(auto_now_add=True ,verbose_name='Envoyé ')

	def __str__(self):
		return self.email