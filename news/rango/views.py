from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	context_dict = {'boldmessage': 'test'}
	return render(request, 'rango/index.html', context=context_dict)

