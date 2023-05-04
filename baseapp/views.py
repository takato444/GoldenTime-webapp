from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
def into_index(request):
    if request.user.is_authenticated:
    	   name=request.user.username
    return render(request,'main.html',locals())
def into_sign(request):
    pass
def into_upload(request):
    return render(request,'photo.html',locals())
def comment(request):
    pass
def search(request,searchname):
    pass
def into_mylove(request):
    return render(request,'mylove.html',locals())
def into_mypost(request):
    return render(request,'mypost.html',locals())
def into_sigin(request):
    return render(request,'sigin.html',locals())
def logout(request):
    auth.logout(request)
    return redirect('/')
def login(request):
	if request.method == 'POST':
		name = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=name, password=password)
		if user is not None:
			if user.is_active:
				auth.login(request,user)
				return redirect('/')
				# message = '登入成功！'
			else:
				message = '帳號尚未啟用！'
		else:
			message = '登入失敗！'
	return render(request, "login.html", locals())
def addtestuser(request):	
	try:
		user=User.objects.get(username="test")
	except:
		user=None
	if user!=None:
		message = user.username + " 帳號已建立!"
		return HttpResponse(message)
	else:	# 建立 test 帳號			
		user=User.objects.create_user("test","test@test.com.tw","password")
		user.first_name="takato" # 姓名
		user.last_name="togakushi"  # 姓氏
		user.is_staff=True	# 工作人員狀態
		user.save()
		return redirect('/admin/')
def sigin(request):
    if request.method == 'POST':
        fname = request.POST[fname]
        lname = request.POST[lname]
        password = request.POST[password]
        username = request.POST[username]
        email = request.POST[email]
        user.first_name = fname
        user.last_name = lname
        user=User.objects.create_user(username,email,password)
        user.save()
    return render(request,'sigin.html',locals())
# Create your views here.
