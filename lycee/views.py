from django.shortcuts import render
from django.http import HttpResponse
from .models import Cursus
from django.template import loader

# Create your views here.

#def index(request):
#  return HttpResponse("Racine de lycee")

def detail(request,cursus_id):
  resp = 'result for cursus {}'.format(cursus_id)
  return HttpResponse(resp)

def index(request):
  #result_list = Cursus.objects.order_by('name')
  result_list = Cursus.objects.all()

  #template = loader.get_template('lycee/index.html')

  context = {
    'liste' : result_list,
  }
  
  #return HttpResponse(template.render(context,request))

  return render(request, 'lycee/index.html', context)