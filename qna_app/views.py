from django.shortcuts import render,redirect
from .models import QuestionModel,CategoryModel
from .forms import QuestionForm
from django.http import HttpResponse
from django.views.generic import CreateView,ListView

#Create your views here
class QuestionModelCreateView(CreateView):
    model = QuestionModel
    fields = '__all__'
class QuestionModelListView(ListView):
    model = QuestionModel
    queryset = QuestionModel.objects.all()


def vote_question(request,id):
    instance = QuestionModel.objects.get(id = id)
    vote = instance.question_vote + 1
    instance.question_vote = vote
    instance.save()
    return redirect('qna:read')

def addquestion(request):
    if request.method == "POST":
        form = QuestionForm(request.POST,request.FILES)
        if form.is_valid():
            try:
                form.save()
                return HttpResponse("sucessfully submitted")
            except:
                return HttpResponse("Failed,Try Again!")
        else:
            print(form.errors)
            return HttpResponse(form.errors)
    else:
        #form = QuestionForm
        category = CategoryModel.objects.all()
        return render(request,'questionmodel_create.html',context = {'category' : category})

# def question(request):
#     question = QuestionModel.objects.all()
#     return render(request,'question.html',context = {'q' : question})

def questionlist(request):
    question = QuestionModel.objects.all()
    return render(request,'questionmodel_list.html',context = {'q' : question})

def update_question(request,id):
    question = QuestionModel.objects.get(id = id)

    if request.method=="POST":

        form = QuestionForm(request.POST,request.FILES,instance = question)
        if form.is_valid():
            try:
                form.save()
                return redirect('qna:read')
            except:
                return HttpResponse("Failed,Try Again!")
        else:
            print(form.errors)
            return HttpResponse(form.errors)
    else:
        form = QuestionForm(instance=question)
        return render(request,'questionmodel_update.html',context = {'form' : form})

def delete(request,id):
    question = QuestionModel.objects.get(id=id)
    question.delete()
    return redirect('qna:read')
    





