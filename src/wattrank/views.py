from .models import wattmodel
from django.http import HttpResponse

def index(request):
	all_data=wattmodel.objects.all()
	html=''
	for data in all_data:
		html+=data.income 
	
	return HttpResponse(html)
