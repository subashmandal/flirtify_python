from django.contrib import admin
from django.urls import path

from home import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home page'),
    path('profile/', views.profile, name = 'profile page')
]
