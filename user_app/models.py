from django.db import models

# Create your models here.
class QuestionModel(models.Model):
    title = models.CharField(max_length = 255)
    posted_user = models.CharField(max_length = 120)
    timestamp = models.DateTimeField(auto_now_add= True)
    question_desp = models.TextField()
    question_img = models.ImageField(upload_to = 'QuestionImg')

class AnswesrModel(models.Model):
    answered_by = models.CharField(max_length = 120)
    timestamp = models.DateTimeField(auto_now_add= True)
    question = models.Foreign(QuestionModel,on_delete = models.CASCADE )
    votes = models.IntegerField
    is_accept = models.BooleanField
    answer_desp = models.TextField()
    answer_img = models.ImageField(upload_to = 'AnswerImg')
    


    