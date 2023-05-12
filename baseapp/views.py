from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from baseapp.models import basedata
from .forms import foodform
def admin(request):
	return redirect('/admin/')
def into_index(request):
    if request.user.is_authenticated:
    	   name=request.user.username
    return render(request,'main.html',locals())
def into_sign(request):
    pass
def into_upload(request):
	if request.method =='POST':
		form = foodform(request.POST,request.files)
		if form.is_valid():
			form.save()
		return redirct('/')
	else:
		form = foodform()
		context = {
            'form': form
        }
	# return render(request.'photo.html',locals())
	return render(request,'photo.html',locals())
def comment(request):
    pass
def search(request,searchname):
    pass
def into_mylove(request):
    return render(request,'mylove.html',locals())
def myinfo(request):
	if request.user.is_authenticated:
		username = request.user.username
		data = basedata.objects.filter(username__exact=username)
		# data_list = list(data)
		# sex = data_list
		# birthday = data.birthday
		# info = data.info
		# phone = data.phone
		return render(request,'myinfo.html',locals())
	else:
		return redirect('login/')
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
def addtestdata(request):
	fname = "takato"
	lname = "togakushi"
	username = "test"
	birthday = "2004-05-09"
	sex = 'M'
	phone = "087654321"
	info = "我是測試資料"
	email = "test@test.com.tw"
	unit = basedata.objects.create(username=username,fname=fname,lname=lname, sex=sex, birthday=birthday,email=email,phone=phone, info=info) 
	unit.save()  #寫入資料庫
	return redirect('/showdata/')
def showdata(request):
	data = basedata.objects.all().order_by('id')
	return render(request,'showdata.html',locals())
def delete(request,id=None):  #刪除資料
	if id!=None:
		if request.method == "POST":  #如果是以POST方式才處理
			id=request.POST['id'] #取得表單輸入的編號
		try:
			unit = basedata.objects.get(id=id)  
			unit.delete()
			return redirect('/')
		except:
			message = "讀取錯誤!"			
	return render(request, "delete.html", locals())	
def edit(request,id=None,mode=None):  
	if mode == "edit":  # 由 edit.html 按 submit
		unit = student.objects.get(id=id)
		unit.username=request.GET['username']  #取得要修改的資料記錄
		unit.fname=request.GET['fname']
		unit.lname=request.GET['lname']
		unit.sex=request.GET['sex']
		unit.birthday=request.GET['birthday']
		unit.email=request.GET['email']
		unit.phone=request.GET['phone']
		unit.info=request.GET['info']		
		unit.save()  #寫入資料庫
		message = '已修改...'
		return redirect('/')	
	else: # 由網址列
		try:
			unit = basedata.objects.get(id=id)  #取得要修改的資料記錄
			strdate=str(unit.birthday)
			strdate2=strdate.replace("年","-")
			strdate2=strdate.replace("月","-")
			strdate2=strdate.replace("日","-")
			unit.birthday = strdate2
		except:
			message = "此 id不存在！"	
		return render(request, "edit.html", locals())	
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
	try:
		if request.method == 'POST':
			fname = request.POST['fname']
			lname = request.POST['lname']
			sex = request.POST['sex']
			password = request.POST['password']
			username = request.POST['username']
			email = request.POST['email']
			birthday = request.POST['birthday']
			user = User.objects.create_user(username,email,password)
			user.first_name=fname
			user.last_name=lname
			user.is_staff=False
			user.save()
			unit = basedata.objects.create(username=username,fname=fname,lname=lname, sex=sex, birthday=birthday,email=email,phone=phone, info=info) 
			unit.save()  #寫入資料庫
			return redirect('/')
	except:
		message = "帳號已經存在"
		return redirect('/')
	return render(request,'sigin.html',locals())
# Create your views here.
