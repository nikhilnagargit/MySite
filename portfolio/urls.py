from django.urls import path,include

from . import views

app_name = 'portfolio'
urlpatterns = [
  
       path('about/',views.aboutview,name='about'),
       path('projects/',views.projectview,name='projects'),
       path('contact/',views.contactview,name = 'contacts'),
       path('photocards/',views.PhotocardListView.as_view(),name ='photocardlist'),
       path('projects/',include('django.contrib.auth.urls')),
       path('projects/new',views.ProjectCreateView.as_view(),name ='projectcreate'),


          


]
  