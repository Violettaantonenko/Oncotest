from django.contrib import admin
from .models import *

admin.site.register (Doctors)
admin.site.register (Clients)
admin.site.register (DoctorsSpecialization)
admin.site.register (DoctorsRating)
admin.site.register (ResearchesRating)
admin.site.register (Consultation)
admin.site.register (Research)
# Register your models here.
