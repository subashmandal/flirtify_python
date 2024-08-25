from django.contrib import admin
from django.urls import include, path
# from .import views
from flirtify import views
# from .views import FilteredUserData

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('show', views.showUserData,name='showUserData'),
    path('filterdata', views.filterData,name='filterdata'),
    path('adduserdata', views.addUserData,name='adduserdata'),
    path('updateuserdata', views.updateUserData,name='updateuserdata'),
    path('api/deleteuserdata', views.deleteUserData,name='deleteUserData'),
    path('login/', views.loginPage,name='login page'),
    path('signup/', views.signupPage,name='signup page'),
]
