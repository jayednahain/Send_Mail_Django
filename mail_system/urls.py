from .import views

from django.urls import path,include
from .views import AllMailView
from .views import MailDetailView
from .views import DeleteMail

urlpatterns = [

   path('sendemail/', views.sendemail, name='send_email_link'),
   path('savemaildatabase/', views.save_mail, name='save_mail_link'),
   path('viewallmail/',AllMailView.as_view(),name='mail_sent_item_link'),
   path('ViewSingleMail/<int:pk>',MailDetailView.as_view(),name='view_single_mail_link'),
   path('DeleteMail/<int:pk>',DeleteMail.as_view(),name='delete_mail_link')
]