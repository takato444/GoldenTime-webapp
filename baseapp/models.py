from django.db import models
from django.utils import timezone
class basedata(models.Model):
    username = models.CharField(max_length=20,null = False,primary_key = True)
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
    username=models.ForeignKey(basedata,on_delete=models.CASCADE)
    upload_date = models.DateField(default=timezone.now)
class mesg(models.Model):
    mes_no = models.AutoField(primary_key = True)
    context =models.CharField(max_length = 255)
    username = models.ForeignKey(basedata,on_delete = models.CASCADE)
    food_no = models.ForeignKey(food, on_delete = models.CASCADE)
