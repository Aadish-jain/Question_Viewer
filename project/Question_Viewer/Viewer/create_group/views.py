from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView,CreateView
from django.core.files.storage import FileSystemStorage
# from django.urls import reverse_lazy

from .forms import CreateGroupForm,QuestionsForm

from .models import CreateGroup,Questions
from create_group.models import Questions
# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'


def create_group(request):
    context = {}
    if request.method == 'POST':
        form = CreateGroupForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateGroupForm()
    return render(request,'group.html',{'form':form })


def upload_question(request):
    if request.method == 'POST':
        form1 = QuestionsForm(request.POST, request.FILES)
        if form1.is_valid():
            form1.save()
            return redirect('question_list')
    else:
        form1 = QuestionsForm()
    return render(request, 'upload_question.html', {
        'form': form1
    })


def question_list(request):
    questions = Questions.objects.all()
    # print(questions)
    return render(request, 'question_list.html', {
        'questions': questions
    })



def delete_question(request, pk):
    if request.method == 'POST':
        book = Questions.objects.get(pk=pk)
        book.delete()
    return redirect('question_list')
