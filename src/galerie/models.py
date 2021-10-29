from django.db import models

# Create your models here.
# GESTION DE LA GALERIE D'IMAGE
class Gallery(models.Model):
	title = models.CharField(max_length=80 ,verbose_name='Titre', default='Galerie')
	big_size_pic = models.ImageField(verbose_name='grande image')
	small_size_pic = models.ImageField(verbose_name='petite image')


	class Meta:
		verbose_name = 'Galerie'
		verbose_name_plural = 'Galeries'

	def __str__(self):
		return f'{self.title}'
		

