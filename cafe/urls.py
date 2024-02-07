
from django.contrib import admin
from django.urls import path,include
from cafe import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('blog', views.blog,name='blog'),
    path('about-us', views.about,name='about'),
    path('contact-us',views.contact,name='contact'),
    path('service',views.service,name='service'),
    path('404', views.error,name='error'),
    path('forms', views.forms,name='forms'),
    path('submitform', views.submitform,name='submitform'),
    path('marksheet', views.marksheet, name= 'marksheet'),
    path('contact-us', views.getcontact ,name='getcontact'),
    path('newsdetails/<slug>',views.newsdetails),
    # path('api-auth/',include('rest_framework')),

]

handler404 = 'cafe.views.custom_404_view'

