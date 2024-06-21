from django.urls import path
from HR import views

urlpatterns = [
    path('Signin/',views.Loginview.as_view(),name='signin'),
    path('index/',views.Dashboard.as_view(),name='index'),
    path('signout/',views.Signout.as_view(),name='logout'),
    path('category/',views.Addcategory.as_view(),name='category'),
    path('category/<int:pk>',views.Categoryremove.as_view(),name='categorydelete'),
    path('jobadd/',views.Addjob.as_view(),name='addjob'),
    path('jobdel/<int:pk>',views.Deljob.as_view(),name='jobdel'),
    path('joblist/',views.Joblist.as_view(),name='joblist'),
    path('jobedit/<int:pk>',views.Jobupdate.as_view(),name='edit'),
    path('jobview/<int:pk>',views.Jobview.as_view(),name='view'),
]

