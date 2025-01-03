from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.VoteView,name='voteview'),
    path('candidates/', views.CandidatesView, name='candidatesview'),
    path('contact/',views.ContactView,name='contactview'),
    path('ro/',views.RoView,name='roview'),
    path('voting/',views.VotingView,name='votingview'),
    path('dashboard/',views.DashboardView,name='dashboardview'),
    path('studentview/',views.student_view,name='studentview'),
    path('students/', views.student_list, name='students'),
    path('candidatesregister/', views.CandidatesRegister, name='candidatesregister'),
]
