
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static


from news_api import urls
from  news_api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('student_profile.urls')),
    path('members/',include('django.contrib.auth.urls')),
    path('members/',include('authentication.urls')),
    path('news/',include('news_api.urls')),
    path('attendence/',include('attendance.urls')),
    path('faceRecogantion/',include('face_Recognition.urls')),
    path('MailSystem/',include('mail_system.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
