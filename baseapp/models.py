from django.db import models
class basedata(models.Model):
    username = models.CharField(max_length=20,null = False)
    fname = models.CharField(max_length=20, null=False)
    lname = models.CharField(max_length = 20, null=False)
    sex = models.CharField(max_length=2, default='M', null=False)
    birthday = models.DateField(null=False)
    email = models.EmailField(max_length=100, blank=True, default='')
    phone = models.CharField(max_length=50, blank=True, default='')
    info = models.CharField(max_length=255,blank=True, default='')

    def __str__(self):
        return self.username
# Create your models here.
