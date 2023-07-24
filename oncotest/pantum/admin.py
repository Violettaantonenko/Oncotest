from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


@admin.display(description="Фамилия, имя, отчество")
def upper_case_name(obj):
    return f"{obj.surname} {obj.name} {obj.fathername}".upper()


@admin.display(description='Фото')
def get_html_photo(objects):
    if objects.photo:
        return mark_safe(f'<img src={objects.photo.url} width=50>')


@admin.register(Doctors)
class DoctorsAdmin(admin.ModelAdmin):
    get_html_photo.short_descriptions = 'Фото'
    fields = [('surname', 'name', 'fathername'), 'age', 'specialization', 'experience', get_html_photo]
    list_display = [upper_case_name, 'specialization', 'experience', get_html_photo]
    list_display_links = [upper_case_name]
    ordering = ['surname']
    search_fields = ['surname']
    list_per_page = 10
    list_filter = ['specialization', 'experience']


@admin.display(description="Фамилия, имя, отчество")
def upper_case_name(obj):
    return f"{obj.surname} {obj.name} {obj.fathername}".upper()


@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    fields = [('surname', 'name', 'fathername'), 'age', 'phone', 'email', 'city']
    list_display = [upper_case_name, 'age', 'phone', 'email', 'city']
    list_display_links = [upper_case_name]
    ordering = ['surname']
    search_fields = ['surname', 'phone']
    list_per_page = 10
    list_filter = ['age', 'city']


@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ['date', 'service', 'clients', 'phone']
    ordering = ['date']


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['clients', 'rating', 'description']


@admin.register(DoctorsSpecialization)
class DoctorsSpecializationAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(Research)
class Research(admin.ModelAdmin):
    list_display = ['name', 'description', 'photo']
