from django.db import models

class Owner(models.Model):
    owner_name=models.CharField(max_length=50)
    owner_username=models.CharField(max_length=30)
    owner_email=models.EmailField(max_length=100)
    owner_mobile=models.CharField(max_length=15,   default=0)
    owner_passward=models.CharField(max_length=500)
    owner_confirmpass=models.CharField(max_length=500)

    objects = models.Manager()

    def __str__(self):
        return self.Owner_name

class User(models.Model):
    user_name=models.CharField(max_length=50)
    user_username=models.CharField(max_length=30)
    user_email=models.EmailField(max_length=100)
    user_city=models.CharField(max_length=50)
    user_passward=models.CharField(max_length=1000)
    user_confirmpass=models.CharField(max_length=1000)
    
    def __str__(self):
        return self.user_name
    

class rooms(models.Model):
    p_type=models.CharField(max_length=20)
    p_name=models.CharField(max_length=50)
    p_adress=models.CharField(max_length=100)
    p_city=models.CharField(max_length=50)
    p_email=models.EmailField(max_length=100 , default="None")
    vacancy=models.IntegerField(default=0)
    p_monthly=models.IntegerField()
    p_facilities=models.CharField(max_length=100)
    p_img=models.ImageField(upload_to="images/",default="")

    
    def __str__(self):
        return self.p_type
    
class Contact(models.Model):
    c_name=models.CharField(max_length=50)
    c_email=models.EmailField(max_length=100)
    c_msg=models.CharField(max_length=30)
   

    objects = models.Manager()

    def __str__(self):
        return self.Owner_name