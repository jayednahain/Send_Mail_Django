from django import forms
from .models import Mailbox


class Mailform(forms.ModelForm):
   class Meta:
      model=Mailbox
      fields ="__all__"
