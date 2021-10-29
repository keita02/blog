from .models import Gallery

def gallery_image(request):
	galerie_image = Gallery.objects.all()

	return dict(galerie_image=galerie_image)