from django.db import models
from tinymce import models as tinymce_models
from ckeditor.fields import RichTextField
# Create your models here.
class Dernieretendance(models.Model):
	title = tinymce_models.HTMLField(blank=True, null=True ,verbose_name='Titre de la derniere tendance')
	content = tinymce_models.HTMLField(blank=True, null=True ,verbose_name='Contenu de la derniere tendance')

	class Meta:
		verbose_name = 'Dernière tendance'
		verbose_name_plural = 'Dernière tendance'

