from django.urls import path
from . import views

urlpatterns = [
    # pages
    path('', views.dashboard, name='dashboard'),
    path('movie/', views.movie, name='movie'),
    path('user/', views.user, name='user'),
    path('login/', views.login, name='login'),
    # function
    path('login_check/', views.login_check, name='login_check'),
    path('logout/', views.logout, name='logout'),
    path('open_file/', views.open_file, name='open_file'),
    path('open_folder/', views.open_folder, name='open_folder'),
    path('get_info/', views.get_info, name='get_info'),
    path('movie_list/', views.movie_list, name='movie_list'),
]
