from django.urls import path
from jobseeker import views


urlpatterns = [
    path('register/',views.Register.as_view(),name='reg'),
    path('signout/',views.Signout.as_view(),name='logout'),
    path('seeker/',views.Student_home.as_view(),name='seekerindex'),
    path('seekerprofile/',views.Profile.as_view(),name='seekerprofile'),
    path('profileview/<int:pk>',views.Profileview.as_view(),name='p_view'),
    path('profileupdate/<int:pk>',views.update_profile.as_view(),name='p_edit'),
    path('jobdetail/<int:pk>',views.jobdetail.as_view(),name='job_detail'),
    path('applyjob/<int:pk>',views.job_apply.as_view(),name='applyjob'),
    path('applied/',views.Applied_job.as_view(),name='applied'),
    path('delete_job/<int:pk>',views.Delete_job.as_view(),name='deljob'),

]