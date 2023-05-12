from django import forms
from .models import food

class PostForm(forms.Form):
	username = forms.CharField(max_length=20,initial='')
	fname = forms.CharField(max_length=20,initial='')
	lname = forms.CharField(max_length=20,initial='')
	sex = forms.CharField(max_length=2,initial='M')	
	birthday = forms.DateField()
	email = forms.EmailField(max_length=100,initial='',required=False)
	phone = forms.CharField(max_length=50,initial='',required=False)
	info = forms.CharField(max_length=255,initial='',required=False)
class foodform(forms.ModelForm):
	class Meta:
		model = food
		fields = '__all__'
