from django.contrib import admin
from .models import CategoryModel,QuestionModel,AnswesrModel 
# Register your models here.
admin.site.register(CategoryModel)
admin.site.register(QuestionModel)
admin.site.register(AnswesrModel)


