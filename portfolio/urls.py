from django.urls import path
from django.conf import include
from . import views
from django.contrib.auth import views as auth_views
app_name = 'portfolio'
urlpatterns = [
  
       path('about/',views.aboutview,name='about'),
       path('projects/',views.projectview,name='projects'),
       path('contact/',views.contactview,name = 'contacts'),
       path('photocards/',views.PhotocardListView.as_view(),name ='photocardlist'),


          


]
 