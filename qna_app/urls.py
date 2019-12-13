from django.urls import path,include
from .views import addquestion, questionlist ,update_question,delete,QuestionModelCreateView,QuestionModelListView,vote_question,answerlist,addanswer,questiondetail,test,detail


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
    path('answer/',answerlist,name = 'answer'),
    path('addanswer/',addanswer,name ='addanswer'),
    path('detail/<int:id>/',questiondetail,name='detail'),
    path('detaill/<int:id>/',detail,name='detail'),
    path('test/',test,name ='test')
]