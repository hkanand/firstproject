from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from . import forms
from main.models import User, Question ,Answer

# Create your views here.
def homePageView(request):
	return HttpResponse("hello world")

def test(request):
	return render(request,'test.html',{})

def signup(request):
	if request.method =='GET':
		form =forms.UserForm()
	else :
		form = forms.UserForm(request.POST)
		if  form.is_valid():
			objects=form.save()
			return HttpResponse("Form submitted Sucessfully")


	context = { 
	            'user_form': form
	}
	return render(request,'signup.html',context)

def dashboard(request):
		user_id=request.GET.get("user_id")
		user=User.objects.filter(id=user_id)
		questions=Question.objects.all
		print(questions)
		context= {
		"user" : user[0],
		"questions": questions
		}
		return render(request,'dashboard.html',context)
	
def login(request):
	if request.method =='GET':
		form =forms.UserLoginForm()
		context = {"UserLoginForm": form}
		return render(request,"ulogin.html",context)

	else :
		form = forms.UserLoginForm(request.POST)
		email=form.data["email"]
		password= form.data["password"]
		print( email,password)
		user=User.objects.filter(email=email ,password=password)
		print(user)
		if len(user)> 0:
			return HttpResponseRedirect('/dashboard/?user_id=' + str(user[0].id))
			#return HttpResponse(" Sucessfully login")
		
		else:
			context={"UserLoginForm": form}
			return render(request,'ulogin.html',context)


def question(request):
	if request.method =='GET':
		user_id=request.GET.get("user_id")
		form =forms.QuestionForm()
		context={
		      'question_form':form,
		      'user_id': user_id
		}
		return render(request,'question.html',context)
	else :
		form = forms.QuestionForm(request.POST)
		if form.is_valid():
			objects = form.save(commit= False)
			print("\n\n\nthis is user id \n\n",form.data["user_id"])
			user=User.objects.filter(id=form.data["user_id"])[0]
			objects.user = user
			objects.save()
			return HttpResponseRedirect('/dashboard/?user_id=' + str(form.data["user_id"]))

	

def answer(request):
		if request.method =='GET':

			user_id=request.GET.get("user_id")
			question_id = request.GET.get("question_id")
			form =forms.AnswerForm()
			context={'AnswerForm': form,'user_id' :user_id,'question_id': question_id }
			return render(request,'answer.html',context)
		else :
			form = forms.AnswerForm(request.POST)
			if form.is_valid():
				objects = form.save(commit=False)
				print("\n\n\n this is user id \n\n",form.data["user_id"])
				user=User.objects.filter(id=form.data["user_id"])[0]
				print(user)
				objects.user = user
				print(form.data)
				question_id = form.data["question_id"]
				print(question_id)
				objects.question_id= question_id
				objects.save()
			return HttpResponseRedirect('/dashboard/?user_id='+str(form.data["user_id"]))
def upvote(request):
	user_id=request.GET.get("user_id")
	answer_id=request.GET.get("answer_id")
	answer=Answer.objects.get(id=answer_id)
	upvotes=answer.upvotes
	answer.upvotes=upvotes+1
	answer.save()
	return HttpResponseRedirect('/dashboard/?user_id='+str(user_id))

def downvote(request):
	user_id=request.GET.get("user_id")
	answer_id=request.GET.get("answer_id")
	answer=Answer.objects.get(id=answer_id)
	downvotes=answer.downvotes
	answer.downvotes=downvotes+1
	answer.save()
	return HttpResponseRedirect('/dashboard/?user_id='+str(user_id))

					



					

			

	 
	
