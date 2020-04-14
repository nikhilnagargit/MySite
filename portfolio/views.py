from django.shortcuts import render
from . import models 
from  django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def aboutview(request):
	return( render(request,'portfolio/about.html'))

def projectview(request):
	context = {}
	context['projects'] = models.Project.objects.all()
	context['certificates']=models.Certificate.objects.all()
	return( render(request,'portfolio/projects.html',context))

class ProjectCreateView(LoginRequiredMixin,CreateView):
	model = models.Project
	fields = '__all__'

class ProjectDetailView(DetailView):
	model = models.Project

class ProjectDeleteView(LoginRequiredMixin,DeleteView):
	model = models.Project
	success_url = reverse_lazy('portfolio:projects')

class CertificateCreateView(LoginRequiredMixin,CreateView):
	model = models.Certificate
	fields='__all__'

class CertificateDeleteView(LoginRequiredMixin,DeleteView):
	model = models.Certificate
	success_url= reverse_lazy('portfolio:projects')



def contactview(request):
	return( render(request,'portfolio/contacts.html'))

class PhotocardListView(ListView) :
	model = models.Photocard

class PhotocardCreateView(LoginRequiredMixin,CreateView):
	model = models.Photocard
	fields = '__all__'


class PhotocardDeleteView(LoginRequiredMixin,DeleteView):
	model = models.Photocard
	success_url = reverse_lazy('portfolio:photocardlist')



