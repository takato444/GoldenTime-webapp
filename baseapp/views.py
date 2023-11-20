from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from baseapp.models import basedata,food,mesg,love
from tensorflow.keras.models import load_model
from pyimagesearch import config
import output
import numpy as np
import imutils
import cv2
import sys
import collections
# from compiler.ast import flatten
# from .forms import foodform
def admin(request):
	return redirect('/admin/')
def adminpage(request):
    return redirect('admin＿page.html')
def into_index(request):                          
	data = food.objects.all().order_by('hit') #抓推薦食物跟熱門食物
	rank = food.objects.all().order_by('hit')[:3]
	if request.user.is_authenticated:
		name=request.user.username
	return render(request,'main.html',locals())
def into_image_search(request):
	return render(request,'photo-text.html',locals())
def image_search(request):
	if request.method =='POST':
		img  = food.objects.values('food_no','food_img')
		searchTarget = request.POST['search_img']
		searchH=pHash(searchTarget)
		result = []
		for x,i in img.food_no,img.food_img:
			dataH = pHash(i)
			HD = Hamming_distance(searchH,dataH)
			if HD <40:
				result.append(x)
	return render(request,'search.html',locals())
	
def pHash(imgfile): #phash演算法
	"""get image pHash value"""
	img=cv2.imread(imgfile, cv2.CV_LOAD_IMAGE_GRAYSCALE)
	img=cv2.resize(img,(32,32),interpolation=cv2.INTER_CUBIC)
	h, w = img.shape[:2]
	vis0 = np.zeros((h,w), np.float32)
	vis0[:h,:w] = img      
	vis1 = cv2.dct(cv2.dct(vis0))
	vis1.resize(8,8)
	img_list=flat_gen(vis1.tolist()) 
	avg = sum(img_list)*1./len(img_list)
	avg_list = ['0' if i<avg else '1' for i in img_list]
	return ''.join(['%x' % int(''.join(avg_list[x:x+4]),2) for x in range(0,64,4)])
def Hamming_distance(hash1,hash2): 
    num = 0
    for index in range(len(hash1)):
        if hash1[index] != hash2[index]:
            num += 1
    return num 
def flat_gen(x): #flatten
    def iselement(e):
        return not(isinstance(e, collections.Iterable) and not isinstance(e, str))
    for el in x:
        if iselement(el):
            yield el
        else:
            yield from flat_gen(el)
def into_sign(request):
    pass
def into_upload(request):
	if request.user.is_authenticated:
	# return render(request,'photo.html',locals())
		if request.method =='POST':
			context = request.POST['context']
			food_name = request.POST['fdname']
			# username = request.user.username
			username = basedata.objects.get(username=request.user.username)
			# username=request.user.username
			adr = request.POST['adr']
			unit = food.objects.create(food_name=food_name,username=username,adr=adr,context=context)
			_,food_img = request.FILES.popitem()
			food_img = food_img[0]
			unit.food_img = food_img 
			unit.save()
			image = cv2.imread(unit.food_img.path)
			image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
			image = cv2.resize(image, (224, 224))
			image = image.astype("float32")
			mean = np.array([123.68, 116.779, 103.939][::1], dtype="float32")
			image -= mean
			model = load_model(config.MODEL_PATH)
			preds = model.predict(np.expand_dims(image, axis=0))[0]
			i = np.argmax(preds)
			label = config.CLASSES[i]
			if label == "Bread":
				label = "麵包"
			elif label == "Dairy product":
				label ="乳製品"
			elif label =="Dessert":
				label = "甜點"
			elif label =="Egg":
				label="蛋類"
			elif label == "Fried food":
				label = "炸物"
			elif label=="Meat":
				label="肉類"
			elif label =="Noodles/Pasta":
				label="麵類"
			elif label =="Rice":
				label = "飯類"
			elif label=="Seafood":
				label = "海鮮"
			elif label=="Soup":
				label = "湯品"
			elif label=="Vegetable/Fruit":
				label="蔬菜"
			# 麵包、乳製品、甜點、蛋類、炸物、肉類、麵類、飯類、海鮮、湯品、蔬菜
			# Bread,Dairy product,Dessert,Egg,Fried food,Meat,Noodles,Rice,Seafood,Soup,Vegetable
			unit.tag=label
			unit.save()
			return redirect('/mypost/')
		return render(request,'photo.html',locals())
	else:
		return redirect('/login/')
def comment(request,food_no):
	if request.method == "POST":
		temp=food_no
		try:
			username = basedata.objects.get(username=request.user.username)
		except:
			return redirect('/login/')
		food_no = food.objects.get(food_no=food_no)
		comment = request.POST['comment']
		unit = mesg.objects.create(username=username,food_no=food_no,context=comment)
		unit.save()
	return redirect('/quote_post/'+temp)
def name_search(request): #用名稱找
	if request.method == 'POST':
		searchname = request.POST['searchname']
		data = food.objects.filter(food_name__icontains=searchname)
	return render(request,'search.html',locals())
def search(request,searchname):#用tag找
	data = food.objects.filter(tag=searchname)
	return render(request,'search.html',locals())
def into_search(request):
	data = food.objects.all().order_by('food_no')
	return render(request,'search.html',locals())
def into_mylove(request):
	if request.user.is_authenticated:
		username = request.user.username
		data = food.objects.filter(love__username__exact=username)
		# data_list = list(data)
		# sex = data_list
		# birthday = data.birthday
		# info = data.info
		# phone = data.phone
		return render(request,'mylove.html',locals())
	else:
		return redirect('/login/')
def into_mypost(request):
	if request.user.is_authenticated:
		username = request.user.username
		data = food.objects.filter(username__exact=username)
		return render(request,'mypost.html',locals())
	# return render(request,'photo.html',locals())
	else:
		return redirect('/login/')
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
		return redirect('/login/')
def myinfo_edit(request):
	username = request.user.username
	data = basedata.objects.filter(username__exact=username)
	if request.method == 'POST':
		unit = basedata.objects.get(username=username)
		unit.fname=request.POST['fname']
		unit.lname=request.POST['lname']
		unit.sex=request.POST['sex']
		unit.email=request.POST['email']
		unit.phone=request.POST['phone']
		unit.info=request.POST['info']
		try:
			_,photo = request.FILES.popitem()
			photo = photo[0]
			unit.photo = photo
			unit.save()
		except:
			unit.save()
		return redirect('/myinfo/')	
	return render(request,'myinfo_edit.html', locals())
def mysetting(request):
    return render(request,'mysetting.html',locals())
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
	data = basedata.objects.all().order_by('username')
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
def edit(request):
	username = request.user.username
	data = basedata.objects.filter(username__exact=username)
	if request.method == 'POST':
		unit = basedata.objects.get(username=username)
		unit.fname=request.POST['fname']
		unit.lname=request.POST['lname']
		unit.sex=request.POST['sex']
		unit.email=request.POST['email']
		unit.phone=request.POST['phone']
		unit.info=request.POST['info']
		try:
			_,photo = request.FILES.popitem()
			photo = photo[0]
			unit.photo = photo
			unit.save()
		except:
			unit.save()
		return redirect('/myinfo/')	
	return render(request, "myinfo_edit.html", locals())
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
		fname = request.POST['fname']
		lname = request.POST['lname']
		sex = request.POST['sex']
		phone = request.POST['phone']
		info =request.POST['info']
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
		_,photo = request.FILES.popitem()
		photo = photo[0]
		unit.photo = photo  
		unit.save()  #寫入資料庫
		return redirect('/')
	# message = "帳號已經存在"
	# return HttpResponse("error")
	return render(request,'sigin.html',locals())
def quote_post(request,food_no):
	data = food.objects.filter(food_no=food_no)
	user = basedata.objects.filter(food__food_no=food_no)
	# comment = mesg.objects.all().order_by('username')
	comment = mesg.objects.filter(food_no=food_no)
	# unit = food.object.get(food_no = food_no)
	hit = data[0].hit
	hit = hit +1 
	data.update(hit = hit)
	# data.save()
	return render(request,'quote-post.html',locals())
def joinlove(request,food_no):
	if request.user.is_authenticated:
		username = basedata.objects.get(username=request.user.username)
		food_no=food.objects.get(food_no=food_no)
		q = love.objects.filter(username__exact=username,food_no__exact=food_no)
		q=list(q)
		if not q:
			unit = love.objects.create(username=username,food_no=food_no)
			unit.save()
	return redirect('/mylove/')
# Create your views here.
def kill(request,food_no):
	if request.user.is_authenticated:
		unit = food.objects.filter(food_no__exact=food_no)
		unit.delete()
	return redirect('/mypost/')
  #刪除資料
