from django.urls import path,include
from .views import addquestion

urlpatterns = [
    path('addquestion/',addquestion, name ='addquestion')
 
]