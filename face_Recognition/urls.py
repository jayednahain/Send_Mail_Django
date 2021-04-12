
from django.contrib import admin
from django.urls import path,include
from .import views


urlpatterns = [

    path('',views.recognations_page,name="recognation_page_link"),
    path('get_data/',views.get_data,name="get_data_link"),
    path('takeimage/',views.takeImages,name='take_image_link')

]
