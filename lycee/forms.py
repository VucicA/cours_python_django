from django.forms.models import ModelForm
from .models import Student

class StudentForm(ModelForm):
  class Meta :

    #modele
    model = Student

    #les champs qu'on va traiter
    fields = (
      'first_name',
      'last_name',
      'birth_date',
      'email',
      'phone',
      'cursus', 
      'comments',
    )