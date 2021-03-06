"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from lycee import views
from lycee.views import StudentCreateView, StudentEditView, ParticularCallOfRollView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lycee/', views.index, name="index"),
    path('lycee/student/<int:student_id>', views.detail_student, name='detail_student'),
    path('lycee/student/create', StudentCreateView.as_view(), name='create_student'),
    path('lycee/<int:cursus_id>', views.detail_cursus, name='detail_cursus'),
    path('lycee/student/edit/<pk>', StudentEditView.as_view(), name='edit_student'),
    path('lycee/callOfRoll/<int:cursus_id>', views.callOfRoll, name='call_of_roll'),
    path('lycee/particularCallOfRoll', ParticularCallOfRollView.as_view(), name='particular_call_of_roll'),
    path('lycee/callListCursus/<int:cursus_id>', views.callListCursus, name='call_list_cursus'),
    path('lycee/callListStudent/<int:student_id>', views.callListStudent, name='call_list_student'),
]