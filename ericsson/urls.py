from django.urls import path, include
from ericsson import views
from django.conf.urls import url

from .models import EricssonPostComTracker



urlpatterns = [

path('list/', views.ericssontracker_list, name='ericssontracker_list'),
path('<int:pk>/', views.ericssontracker_detail, name='ericssontracker_detail'),
path('new', views.ericssontracker_new, name='ericssontracker_new'),
path('<int:pk>/edit/', views.ericssontracker_edit, name='ericssontracker_edit'),
path('<int:pk>/teamedit/', views.ericssontracker_edit1, name='ericssontracker_edit1'),
url(r'^ericssonexport/csv/$', views.ericssonexport, name='ericssonexport'),
path('search', views.ericssonpostcomsearch, name='ericssonpostcomsearch'),
url(r'^ericssonrsaexport/csv/$', views.ericssonExportRsaTracker, name='ericssonExportRsaTracker'),
path('rsa/new', views.ericssonrsatracker_new, name='ericssonrsatracker_new'),
path('RSA/list/', views.ericssonrsatracker_list, name='ericssonrsatracker_list'),

]