from .models import Banner

def banner_handler(request):
	banniere=Banner.objects.all()

	return dict(banniere=banniere)