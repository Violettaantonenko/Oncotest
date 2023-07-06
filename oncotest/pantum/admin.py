from django.contrib import admin
from .models import *

@admin.display(description="Фамилия, имя, отчество")
def upper_case_name(obj):
    return f"{obj.surname} {obj.name} {obj.fathername}".upper()
@admin.register(Doctors)
class DoctorsAdmin(admin.ModelAdmin):
    fields = [('surname', 'name', 'fathername'), 'age', 'specialization', 'experience']
    list_display =[upper_case_name,'specialization', 'experience']
    list_display_links = [upper_case_name]
    ordering = ['surname']
    search_fields = ['surname']
    list_per_page = 10
    list_filter = ['specialization','experience']
@admin.display(description="Фамилия, имя, отчество")
def upper_case_name(obj):
    return f"{obj.surname} {obj.name} {obj.fathername}".upper()
@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    fields = [('surname', 'name', 'fathername'), 'age', 'phone', 'email','city']
    list_display = [upper_case_name,'age','phone','email','city']
    list_display_links = [upper_case_name]
    ordering = ['surname']
    search_fields = ['surname','phone']
    list_per_page = 10
    list_filter = ['age', 'city']
@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ['date','doctors','clients']
    ordering = ['date']
    list_filter = ['doctors']
@admin.register(ResearchesRating)
class ResearchesRatingAdmin(admin.ModelAdmin):
    list_display = ['research', 'rating', 'description']
    list_filter = ['research']
    list_filter = ['research']
@admin.register(DoctorsRating)
class DoctorsRatingAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'rating', 'description']
    list_filter = ['doctor']


@admin.register(DoctorsSpecialization)
class DoctorsSpecializationAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(Research)

