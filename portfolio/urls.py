from django.urls import path,include
from . import views

app_name = 'portfolio'
urlpatterns = [
  
       path('about/',views.aboutview,name='about'),
       path('projects/',views.projectview,name='projects'),
       path('contact/',views.contactview,name = 'contacts'),
       path('photocards/',views.PhotocardListView.as_view(),name ='photocardlist'),
       path('photocards/new',views.PhotocardCreateView.as_view(),name ='createphotocard'),
       path('photocards/<pk>/delete',views.PhotocardDeleteView.as_view(),name ='deletephotocard'),
       path('projects/new/',views.ProjectCreateView.as_view(),name ='projectcreate'),
       path('projects/<pk>/',views.ProjectDetailView.as_view(),name ='projectdetail'),
       path('projects/<pk>/delete',views.ProjectDeleteView.as_view(),name = 'deleteproject'),
       path('projects/newcertificate/',views.CertificateCreateView.as_view(),name ='certificatecreate'),
       path('projects/<pk>/certificatedelete',views.CertificateDeleteView.as_view(),name = 'deletecertificate'),
    


          


]
  