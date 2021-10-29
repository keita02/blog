from django.db import models
from tinymce import models as tinymce_models
from ckeditor.fields import RichTextField

# Create your models here.
class DivideSection(models.Model):
	title = tinymce_models.HTMLField(blank=True, null=True ,verbose_name='Titre de la section divide')
	image = models.ImageField()

	class Meta:
		verbose_name = 'Partie section'
		verbose_name_plural = 'Partie section'