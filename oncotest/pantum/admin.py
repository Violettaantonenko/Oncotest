from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


@admin.display(description="Фамилия, имя, отчество")
def upper_case_name(obj):
    return f"{obj.surname} {obj.name} {obj.fathername}".upper()


@admin.register(Doctors)
class DoctorsAdmin(admin.ModelAdmin):
    fields = [('surname', 'name', 'fathername'), 'age', 'specialization', 'experience', 'photo']
    list_display = [upper_case_name, 'specialization', 'experience', 'photo']
    list_display_links = [upper_case_name]
    ordering = ['surname']
    search_fields = ['surname']
    list_per_page = 10
    list_filter = ['specialization', 'experience']

    # def get_photo(self, obj):
    #     return mark_safe(f'<img src={obj.photo.url} width="50">')
    #
    # get_photo.short_description = 'Изображение'
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
    list_display = ['date', 'doctors', 'clients']
    ordering = ['date']
    list_filter = ['doctors']


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['clients', 'rating', 'description']


@admin.register(DoctorsSpecialization)
class DoctorsSpecializationAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(Research)
class Research(admin.ModelAdmin):
    list_display = ['name', 'description', 'photo']
