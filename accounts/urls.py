from django.urls import path
from accounts import views
urlpatterns = [
   path('',views.index,name='index'),
   path('logout',views.logout,name='logout'),

 
  # Password Reset URLs
   path('password_reset/', views.password_reset_request, name='password_reset'),
   path('password_reset_done/', views.password_reset_done, name='password_reset_done'),
   path('reset/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
   path('reset/done/', views.password_reset_complete, name='password_reset_complete'),
    


]