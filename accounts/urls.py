from django.urls import path
from accounts import views
urlpatterns = [
   path('',views.index,name='index'),
   path('logout',views.logout,name='logout')


]