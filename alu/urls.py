from django.urls import path
from alu import views
from django.conf.urls import url


urlpatterns = [

path('list/', views.alutracker_list, name='alutracker_list'),
path('<int:pk>/', views.alutracker_detail, name='alutracker_detail'),
path('new', views.alutracker_new, name='alutracker_new'),
path('<int:pk>/edit/', views.alutracker_edit, name='alutracker_edit'),
path('<int:pk>/teamedit/', views.alutracker_edit1, name='alutracker_edit1'),
url(r'^Aluexport/csv/$', views.Alu_Export, name='Alu_Export'),
path('search', views.alusearch, name='alusearch'),
path('aludashboard', views.AluTrackerListView.as_view(), name='aludashboard'),
path('aludashboard1', views.AluTrackerListView1.as_view(), name='aludashboard1'),

path('alursatracker/new', views.Alursatracker_new, name='Alursatracker_new'),
path('alursatracker/list', views.Alursatracker_list, name='Alursatracker_list'),
url(r'^exportalursatracker/csv/$', views.AluExportRsaTracker, name='AluExportRsaTracker'),
path('alursasearch', views.Alursasearch, name='alursasearch'),
path('<int:pk>/Alursa/edit/', views.Alursatracker_edit, name='Alursatracker_edit'),
path('<int:pk>/Alursa/teamedit/', views.Alursatracker_edit1, name='Alursatracker_edit1'),


]