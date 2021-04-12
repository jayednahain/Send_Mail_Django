from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy


from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import TemplateView

from student_profile.models import Students
from student_profile.models import Department



from .forms import CreateStudentForm,UpdateStudentInformation
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import requests


# Create your views here.


class HomeView(TemplateView):
   template_name = 'home.html'

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['data']=Students.objects.all()

      return context




class StudentListView(ListView):
   model = Students

   depts = Department.objects.all()
   template_name = 'student_list.html'

   def get_context_data(self, *args, **kwargs):
      Dept_menu = Department.objects.all()
      context = super(StudentListView, self).get_context_data(*args, **kwargs)

      context["department_menu"] = Dept_menu

      return context



def search_student(request):
   if 'term' in request.GET:
      qs = Students.objects.filter(name__icontains=request.GET.get('term'))
      student_names = list()
      for student in qs:
         student_names.append(student.name)
      # titles = [product.title for product in qs]
      return JsonResponse(student_names, safe=False)
   return render(request,'student_search.html')



def search_by_id(request):
   if 'term' in request.GET:
      qs = Students.objects.filter(student_id__icontains=request.GET.get('term'))
      student_id_list = list()
      for student_id in qs:
         student_id_list.append(student_id.student_id)
      # titles = [product.title for product in qs]
      return JsonResponse(student_id_list, safe=False)
   return render(request,'student_search_by_id.html')







class ProfileView(DetailView):
   model = Students
   template_name = 'profile_view_with_class.html'

   def get_context_data(self, *args, **kwargs):
      Dept_menu = Department.objects.all()
      context = super(ProfileView, self).get_context_data(*args, **kwargs)

      context["department_menu"] = Dept_menu

      return context


class AddStudentView(CreateView):
   form_class = CreateStudentForm
   model = Students
   template_name = 'add_student.html'

   #we have define fields on form.py
   #fields = '__all__'
   def get_context_data(self, *args, **kwargs):
      Dept_menu = Department.objects.all()
      context = super(AddStudentView, self).get_context_data(*args, **kwargs)

      context["department_menu"] = Dept_menu

      return context

class CreateDepartment(CreateView):
   #form_class = CreateStudentForm
   model = Department
   template_name = 'create_department.html'
   fields = '__all__'
   def get_context_data(self, *args, **kwargs):
      Dept_menu = Department.objects.all()
      context = super(CreateDepartment, self).get_context_data(*args, **kwargs)

      context["department_menu"] = Dept_menu

      return context


def department_view(request,dept):

   filter_by_dept = Students.objects.filter(student_department=dept)

   return render(request,'view_by_department.html',{'dept':dept,'filter_by_dept':filter_by_dept})

class UpdateInformationView(UpdateView):
   form_class = UpdateStudentInformation
   model = Students
   template_name = 'Update_student_information.html'


class DeleteStudent(DeleteView):
   model = Students
   template_name = 'delete_post_view.html'
   success_url = reverse_lazy('student_list_link')
   def get_context_data(self, *args, **kwargs):
      Dept_menu = Department.objects.all()
      context = super(DeleteStudent, self).get_context_data(*args, **kwargs)

      context["department_menu"] = Dept_menu

      return context













