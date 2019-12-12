from django.db import models

# Create your models here.
class CategoryModel(models.Model):
    title = models.CharField(max_length = 255)
    title_desc = models.TextField()

    def __str__(self):
        return (self.title_desc)

class QuestionModel(models.Model):
    title = models.CharField(max_length = 255)
    posted_user = models.CharField(max_length = 120)
    timestamp = models.DateTimeField(auto_now_add= True)
    question_desc = models.TextField()
    question_img = models.ImageField(upload_to = 'QuestionImg')
    question_vote = models.IntegerField(default = 0)
    category = models.ForeignKey(CategoryModel,on_delete= models.CASCADE)

    #objects = object.Manager() 

    def __str__(self):
        return (self.question_desc)

class AnswesrModel(models.Model):
    answered_by = models.CharField(max_length = 120)
    timestamp = models.DateTimeField(auto_now_add= True)
    question = models.ForeignKey(QuestionModel,on_delete = models.CASCADE )
    answer_votes = models.IntegerField(default=0)
    is_accept = models.BooleanField
    answer_desc = models.TextField()
    answer_img = models.ImageField(upload_to = 'AnswerImg',blank = True,null = True)

    def __str__(self):
        return (self.answer_desc)


   

    