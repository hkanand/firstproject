from django import forms

from . import models
class UserForm(forms.ModelForm):
   class Meta:
   	model=models.User
   	fields= '__all__'

class UserLoginForm(forms.ModelForm):
   class Meta:
   	model=models.User
   	fields= ['email','password']

class QuestionForm(forms.ModelForm):
	class Meta:
		model=models.Question
		fields= ['name']

class AnswerForm(forms.ModelForm):
	class Meta:
		model=models.Answer
		fields=['answer','upvotes','downvotes']
						