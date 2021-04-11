from django.shortcuts import render
from django.http import HttpResponse
from .models import Cursus, Student, Absence
from django.template import loader
from django.views.generic.edit import CreateView, UpdateView
from .forms import StudentForm, ParticularCallOfRollForm
from django.urls import reverse

# Create your views here.

#def index(request):
#  return HttpResponse("Racine de lycee")

def detail_cursus(request,cursus_id):
  result_list = Student.objects.filter(cursus=cursus_id).order_by('last_name')

  context = {
    'liste' : result_list,
    'cursus' : Cursus.objects.get(id=cursus_id)
  }
  return render(request, 'lycee/cursus/detail_cursus.html', context)


def index(request):
  result_list = Cursus.objects.order_by('name')
  #result_list = Cursus.objects.all()

  template = loader.get_template('lycee/index.html')

  context = {
    'liste' : result_list,
  }
  return HttpResponse(template.render(context,request))


def detail_student(request, student_id):
  result_list = Student.objects.get(pk=student_id)

  context = {
    'liste' : result_list,
  }
  return render(request, 'lycee/student/detail_student.html', context)

def callOfRoll(request, cursus_id):
  students = Student.objects.filter(cursus=cursus_id).order_by('last_name')
  cursus = Cursus.objects.get(id=cursus_id)
  print('0')
  if request.POST.get("submit") == 'submit':
    print('1')
    call = Absence()
    for student in students:
      print('2')
      checkbox = "etudiant"+str(student.id)
      if request.POST.get(checkbox) == "on":
        print('3')
        call.student = Student.objects.get(pk=student.id)
        call.date = request.POST.get("date")
        call.isMissing = True
        call.reason = ''
        call.cursus = Cursus.objects.get(pk=cursus.id)
        call.save()

  context = {
    'students' : students,
    'cursus' : cursus
  }
  return render(request, 'lycee/call/createCall.html', context)

def callListCursus(request, cursus_id):
  callList = Absence.objects.filter(cursus = cursus_id)
  cursus = Cursus.objects.get(id=cursus_id)

  context = {
    'liste' : callList,
    'cursus' : cursus
  }
  
  return render(request, 'lycee/call/callListCursus.html', context)

def callListStudent(request, student_id):
  callList = Absence.objects.filter(student = student_id).filter(isMissing = True)
  student = Student.objects.get(id=student_id)
  count = Absence.objects.filter(student = student_id).filter(isMissing = True).count()

  context = {
    'liste' : callList,
    'student' : student,
    'count' : count
  }
  return render(request, 'lycee/call/callListStudent.html', context)

class StudentCreateView(CreateView):
  # modele
  model = Student
  # formulaire
  form_class = StudentForm
  # template
  template_name = 'lycee/student/create.html'

  def get_success_url(self):
    return reverse('detail_student', args=(self.object.pk,))

class StudentEditView(UpdateView):
  # modele
  model = Student
  # formulaire
  form_class = StudentForm
  # template
  template_name = 'lycee/student/edit.html'

  def get_success_url(self):
    return reverse('detail_student', args=(self.object.pk,))
    

class ParticularCallOfRollView(CreateView):
  # modele
  model = Absence
  # formulaire
  form_class = ParticularCallOfRollForm
  # template
  template_name = 'lycee/call/createParticular.html'

  def get_success_url(self):
    return reverse('index')