from django import forms
from .models import CreateGroup,Questions
from django.forms import ModelForm
    
    

class DateInput(forms.DateInput):
    input_type = 'date'
# class TimeInput(forms.DateInput):
#     input_type = 'time'



class CreateGroupForm(forms.ModelForm):
    class Meta:
        model = CreateGroup
        slug = forms.CharField(max_length=250,widget=forms.HiddenInput())
        slug = id
        fields = ('id','name','created_at')
        widgets = {
            'created_at' : DateInput(),
            # 'timestamp' : TimeInput()
        }

class QuestionsForm(forms.ModelForm): 
    class Meta:
        model = Questions
        question_file = forms.FileField(required=False,label='Question')
        cover = forms.ImageField(required=False,label='Image')
        comment = forms.CharField(required=False)
        # question_file = forms.FileField(required=False)
        fields = ('id','group_id',
        'question_file','cover',
        'comment',
        'created_at')
        widgets = {
            'created_at' : DateInput(),
        }

