from django.shortcuts import render
from .models import DivideSection
# Create your views here.

def section(request):
	divide_section = DivideSection.objects.all()

	return render(request, 'index.html', {'divide_section':divide_section})
