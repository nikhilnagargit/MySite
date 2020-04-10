from django.shortcuts import render
from . import models 
from  django.views.generic import ListView,DetailView,CreateView,DetailView,UpdateView
from django.urls import reverse_lazy
# Create your views here.
def aboutview(request):
	return( render(request,'portfolio/about.html'))

def projectview(request):
	context = {}
	context['projects'] = models.Project.objects.all()
	context['certificates']=models.Certificate.objects.all()
	return( render(request,'portfolio/projects.html',context))


def contactview(request):
	return( render(request,'portfolio/contacts.html'))

class PhotocardListView(ListView) :
	model = models.Photocard

	





