from django.contrib import admin

# Register your models here.
from .models import Student, Cursus

class CursusAdmin(admin.ModelAdmin):
  list_display = ("name", "year_from_bac", "scholar_year")
  fields = ["name", "year_from_bac", "scholar_year"]

class StudentAdmin(admin.ModelAdmin):
  list_display = ("first_name", "last_name", "email", "phone", "cursus")
  #fields = ["first_name", "last_name", "birth_date", "email", "phone", "comments", "cursus"]
  fieldsets = [
    ('main', {'fields': ['first_name', 'last_name', 'birth_date']}),
    ('data', {'fields': ['email', 'phone', 'comments', 'cursus'], 'classes' : ['collapse']})
  ]



admin.site.register(Student, StudentAdmin)
admin.site.register(Cursus, CursusAdmin)