from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from tinymce.models import HTMLField
from tinymce import models as tinymce_models
from ckeditor.fields import RichTextField

# Create your models here.

User = get_user_model()

#----------------------------------------------------------------------------------------------#
# MODELE DU NOMBRE DE VU D'UN ARTICLE
class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='utilisateur ayant vu')
    post = models.ForeignKey('Post', on_delete=models.CASCADE, verbose_name='article vu')

    class Meta:
    	verbose_name='Article vu'
    	verbose_name_plural = 'Articles vus'

    def __str__(self):
        return self.user.username

#----------------------------------------------------------------------------------------------#
# MODELE ASSOCIE A UN EDITEUR D'ARTICLE
class Author(models.Model):
	user        = models.OneToOneField(User, on_delete=models.CASCADE ,verbose_name='Auteur')
	profile_pic = models.ImageField(verbose_name='Photo de profil')

	class Meta:
		verbose_name = 'Editeur'
		verbose_name_plural = 'Editeur'

	def __str__(self):
		return self.user.username


#----------------------------------------------------------------------------------------------#
# MODELE ASSOCIE A UNE CATEGORIE
class Category(models.Model):
	title = models.CharField(max_length=80, verbose_name='Nom de la categorie')

	class Meta:
		verbose_name        = 'Categorie'
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.title 



#----------------------------------------------------------------------------------------------#
# MODELE ASSOCIE A UN ARTICLE
class Post(models.Model):
	title              = models.CharField(max_length=200, verbose_name='Titre')
	overview           = HTMLField('Aperçu', default=' ')
	timestamp          = models.DateTimeField(auto_now_add=True)
	content            = HTMLField('Contenu', default=' ')
	# comment_count      = models.IntegerField(default=0, verbose_name="Nombre de commentaire")
	# view_count         = models.IntegerField(default=0, verbose_name="Nombre de vue")
	author             = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Editeur')
	thumbnail          = models.ImageField(verbose_name="Article Image")
	category           = models.ManyToManyField(Category, verbose_name='Categorie')
	previous_post      = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='precedant', verbose_name='precedent', blank=True, null=True)
	next_post     	   = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='suivant', verbose_name='suivant', blank=True, null=True)
	featured      	   = models.BooleanField(default=False, verbose_name='Publié ?')


	class Meta:
		verbose_name = 'Article'
		verbose_name_plural = 'Articles'

	def get_absolute_url(self):
		return reverse('post', kwargs={'id':self.id})

	def get_update_url(self):
		return reverse('post-update', kwargs={'id':self.id})

	@property
	def get_comments(self):
		return self.comments.all().order_by('-timestamp')

	@property
	def comment_count(self):
		return Comment.objects.filter(post=self).count()

	@property
	def view_count(self):
		return PostView.objects.filter(post=self).count()


	def __str__(self):
		return f'{self.title}'


#----------------------------------------------------------------------------------------------#
# MODELE ASSOCIE A UN COMMENTAIRE
class Comment(models.Model):
	user      = models.ForeignKey(User, on_delete=models.CASCADE ,verbose_name='Auteur du commentaire')
	timestamp = models.DateTimeField(auto_now_add=True, verbose_name='commentaire posté')
	content   = HTMLField(verbose_name='Commentaire')
	# content   = models.TextField(verbose_name='Commentaire')
	post      = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE, verbose_name='Article commenté')

	class Meta:
		verbose_name        = 'Commentaire'
		verbose_name_plural = 'Commentaire'

	def __str__(self):
		return self.user.username



#----------------------------------------------------------------------------------------------#
# GESTION DE LA BANNIERE
class Banner(models.Model):

	# banniere section
	#banner_text = models.CharField(max_length=500, verbose_name="Texte de la banniere", default="Le Blog qui vous rassemble et qui vous ressemble")
	banner_text = tinymce_models.HTMLField(blank=True, null=True ,verbose_name='Texte de la banniere', default='Le Blog qui vous rassemble et qui vous ressemble')
	banner_picture = models.ImageField(verbose_name="L'image de la banniere")
	

	# intro section
	title = tinymce_models.HTMLField(blank=True, null=True ,verbose_name='Titre de texte intro section')
	content = tinymce_models.HTMLField(blank=True, null=True ,verbose_name='Contenu intro section')



	class Meta:
		verbose_name = "Bannière"
		verbose_name_plural = "Bannières"

#----------------------------------------------------------------------------------------------#
