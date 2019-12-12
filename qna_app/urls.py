from django.urls import path,include
from .views import addquestion, questionlist ,update_question,delete,QuestionModelCreateView,QuestionModelListView,vote_question


app_name ='qna'
urlpatterns = [
    path('addquestion/',addquestion, name ='addquestion'),
    path('read/',questionlist, name ='read'),
    path('update/<int:id>/',update_question,name= 'update'),
    path('add/',addquestion,name='add'),
    path('delete/<int:id>/', delete, name ='delete'),
    path('create/', QuestionModelCreateView.as_view(),name ='create'),
    path('li/', QuestionModelListView.as_view(),name ='list'),
     path('upvote/<int:id>/',vote_question,name= 'upvote'),
]