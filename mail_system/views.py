from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse_lazy

from .forms import Mailform

from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import DeleteView


from .models import Mailbox

def sendemail(request):
   if request.method=="POST":
      send_address= request.POST.get('to_emaill')
      text_content = request.POST.get('content')
      subject= request.POST.get('subject')

      subject =subject
      message =text_content
      email_from = settings.EMAIL_HOST_USER
      recipient_list = [send_address]



      send_mail( subject, message, email_from, recipient_list)

      data_save={
         'subject':subject,
         'text_content':text_content,
         'send_address':send_address
      }


      return render(request,'send_email.html',data_save)

   else:

      return render(request,'send_email.html')


def save_mail(request):
   if request.method == "POST":
      form = Mailform(request.POST or None)
      if form.is_valid():
         form.save()
         return render(request,'mail_save_complete.html')
      else:
         return redirect('send_email_link')


class AllMailView(ListView):
   model = Mailbox
   template_name = 'mail_list.html'
   ordering = ['-id']


class MailDetailView(DetailView):
   model = Mailbox
   template_name = 'view_mail.html'


class DeleteMail(DeleteView):
   model = Mailbox
   template_name = 'delete_mail_view.html'
   success_url = reverse_lazy('mail_sent_item_link')


