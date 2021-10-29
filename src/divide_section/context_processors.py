from .models import DivideSection

def section(request):
	mysection = DivideSection.objects.all()

	return dict(mysection=mysection)