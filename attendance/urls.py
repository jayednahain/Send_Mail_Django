from django.urls import path,include
from .import views

urlpatterns = [

   path('',views.welcome_page,name="welecome_page_attendence_link"),
   path('StudentListLocal/',views.student_sql_list,name="student_local_list_link"),
   path('Export/',views.export,name= "export_csv_link")


]
