from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home page'),
    path('profile/', views.profile, name = 'profile page'),
    path('fetch-user-data/', views.fetch_user_data, name = 'fetch_user_data'),
    path('insertUser/', views.insertUser, name = 'insertUser')
]
