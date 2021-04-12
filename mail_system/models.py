from django.db import models
from datetime import datetime
import datetime

class Mailbox(models.Model):
   sent_address = models.EmailField(max_length=40)
   subject = models.CharField(max_length=20)
   content = models.TextField(max_length=300)
   mail_save_Date = models.DateField(auto_now_add=True)



   class Meta:
      ordering = ['-id']




   def __str__(self):
      return self.sent_address