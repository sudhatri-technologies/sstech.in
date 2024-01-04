from django.urls import path
from hrm_admin import views
urlpatterns = [
    path('dashboard/',views.dashboard,name='dashboard'),
    path('add/',views.addUpdateEmployee,name='add'),
    path('manage/',views.manageEmployee,name='manage'),
    path('attendance/',views.attendance,name='attendance'),
    path('update/<str:id>/',views.addUpdateEmployee,name='update'),
    path('delete/<str:id>/',views.deleteEmployee,name='delete'),
    

    # path('update/<int:id>/',views.addUpdateEmployee,name='update'),
    # path('delete/<int:id>/',views.deleteEmployee,name='delete'),
    # # path('cal',views.cal,name='cal'),
   


]