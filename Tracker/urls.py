from django.urls import path
from . import views
from django.conf.urls import url
urlpatterns = [

#path('', views.tracker_list, name='tracker_list'),
path('', views.tracker_list, name='tracker_list'),
path('tracker/<int:pk>/', views.tracker_detail, name='tracker_detail'),
path('tracker/new', views.tracker_new, name='tracker_new'),
path('tracker/<int:pk>/edit/', views.tracker_edit, name='tracker_edit'),
path('tracker/<int:pk>/teamedit/', views.tracker_edit1, name='tracker_edit1'),
url(r'^export/csv/$', views.some_view, name='some_view'),
path('tracker/calculator/', views.Calc_link, name='Calc_link'),
path('tracker/search', views.search, name='search'),
path('tracker/about', views.about, name='about'),
url(r'^password/$', views.change_password, name='change_password'),
#path('assignment/new', views.assignment_new, name='assignment_new'),
path('assignment/<int:pk>/edit/', views.assignment_edit, name='assignment_edit'),
path('assignment/<int:pk>/', views.assignment_detail, name='assignment_detail'),
path('assignment_list', views.assignment_list, name='assignment_list'),
path('password_change_complete', views.password_change_complete, name='password_change_complete'),
path('contact_form', views.contact_form, name='contact_form'),
path('rsatracker/new', views.rsatracker_new, name='rsatracker_new'),
path('rsatracker_list', views.rsatracker_list, name='rsatracker_list'),
url(r'^exportrsatracker/csv/$', views.ExportRsaTracker, name='ExportRsaTracker'),
url(r'^exportrsasearchtracker/$', views.ExportRsaTracker1, name='ExportRsaTracker1'),
path('rsasearch', views.rsasearch, name='rsasearch'),
path('<int:pk>/edit/', views.rsatracker_edit, name='rsatracker_edit'),
path('<int:pk>/teamedit/', views.rsatracker_edit1, name='rsatracker_edit1'),
path('dashboard', views.TrackerListView.as_view(), name='dashboard'),
path('dashboard1', views.TrackerListView1.as_view(), name='dashboard1'),

]