from django.urls import path
from employee import views
urlpatterns = [
    path('checkin/',views.checkIn,name='checkin'),
    path('checkout/',views.checkOut,name='checkout'),
    path('applyleave/',views.applyLeave,name='applyleave'),
    path('dahboard',views.empDashboard,name='empdashboard'),
    path('attendence-history',views.attendenceHistory,name='attendencehistory'),
    path('leave-report',views.leaveReport,name='leavereport')


]