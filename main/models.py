from django.core.validators import MaxValueValidator,MinValueValidator,EmailValidator
from django.db import models

class User(models.Model):
	name=models.CharField(max_length=100)
	age=models.IntegerField(blank=True,null=True,validators=[MaxValueValidator(150),MinValueValidator(0)])
	email=models.CharField(max_length=256,validators=[EmailValidator],null=True,unique=True)
	password=models.CharField(max_length=6,default="111222")
	GENDERS=(
		('F','Female'),
		('M','Male')
          )
	gender=models.CharField(max_length=1,choices=GENDERS)
	def __str__(self):
		return self.name

class Question(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	name=models.TextField(null=False)
	
	def __str__(self):
		return self.name

class Answer(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	question=models.ForeignKey(Question,on_delete=models.CASCADE)
	answer=models.TextField(null=False)
	upvotes=models.IntegerField(null=True,default= 0)
	downvotes=models.IntegerField(null=True,default = 0)
	# def __str__(self):
	# 	return self.answer

						
		
		
	