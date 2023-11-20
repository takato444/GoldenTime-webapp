from django.db import models
from django.utils import timezone
class basedata(models.Model):
    username = models.CharField(max_length=20,null = False,primary_key = True)
    photo = models.ImageField(upload_to='photo/',blank=False,default="image/logo.png")
    fname = models.CharField(max_length=20, null=False)
    lname = models.CharField(max_length = 20, null=False)
    sex = models.CharField(max_length=2, default='M', null=False)
    birthday = models.DateField(null=False)
    email = models.EmailField(max_length=100, blank=True, default='')
    phone = models.CharField(max_length=50, blank=True, default='')
    info = models.CharField(max_length=255,blank=True, default='')
    def __str__(self):
        return self.username
class food(models.Model):
    food_no = models.AutoField(primary_key=True,null= False)
    food_name = models.CharField(max_length=100, null = False)
    food_img = models.ImageField(upload_to='image/', blank=False, null=False)
    context = models.CharField(max_length=225,default="沒有內文喔！")
    adr = models.CharField(max_length=225,default=" ")
    username=models.ForeignKey("basedata",on_delete=models.CASCADE)
    tag = models.CharField(max_length=20,null=False,default="0")
    upload_date = models.DateField(default=timezone.now)
    hit = models.IntegerField(default=0)
class mesg(models.Model):
    mes_no = models.AutoField(primary_key = True)
    context =models.CharField(max_length = 255)
    username = models.ForeignKey("basedata",on_delete = models.CASCADE)
    food_no = models.ForeignKey("food", on_delete = models.CASCADE)
class love(models.Model):
    love_no = models.AutoField(primary_key=True,null=False)
    username = models.ForeignKey("basedata",on_delete=models.CASCADE)
    food_no = models.ForeignKey("food",on_delete=models.CASCADE)
class search(models.Model):
    search_no = models.AutoField(primary_key=True)
    username = models.ForeignKey('basedata',on_delete=models.CASCADE)
    context = models.CharField(max_length=30,default=' ')
