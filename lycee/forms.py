from django.forms.models import ModelForm
from django import forms
from .models import Student, Absence

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
      'comments'
    )

class ParticularCallOfRollForm(ModelForm):
  class Meta :
    #modele
    model = Absence

    #les champs qu'on va traiter
    fields = (
      'date',
      'student',
      'reason',
      'isMissing'
    )
    widgets = {
      'isMissing' : forms.CheckboxInput
    }

class CallOfRollForm(ModelForm):
  class Meta :
    #modele
    model = Absence

    #les champs qu'on va traiter
    fields = (
      'date',
      'isMissing',
      'student'
    )
    widgets = {
        'student' : forms.CheckboxSelectMultiple(),
        'isMissing' : forms.CheckboxInput
    }