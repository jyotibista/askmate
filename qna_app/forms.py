from django import forms 
from .models import QuestionModel,AnswesrModel,CategoryModel


class QuestionForm(forms.ModelForm):
    class Meta:
        model = QuestionModel
        fields = '__all__'