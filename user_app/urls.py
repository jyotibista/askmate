from django.urls import path,include
from .views import login_auth,logout

app_name ='user'

urlpatterns = [
    path('login/',login_auth, name ='login'),
    path('logout/',logout, name ='logout')
]