from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='tracker/AllTrackerHomePage.html'), name='home'), # new]
    path('tracker/', include('Tracker.urls')),
    path('alutracker/', include('alu.urls')),
    path('ericssontracker/', include('ericsson.urls')),

]

