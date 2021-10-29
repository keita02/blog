from .models import Dernieretendance

def tendance(request):
	last_tendance = Dernieretendance.objects.all()
	return dict(last_tendance=last_tendance)