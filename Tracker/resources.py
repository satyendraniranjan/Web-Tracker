from import_export import resources
from .models import *

class TrackerResource(resources.ModelResource):
    class Meta:
        model = Tracker