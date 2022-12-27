from django.shortcuts import render,HttpResponse,redirect
from django.db import connection
from user.models import Owner,Contact,rooms
import mysql.connector as sql
from django.contrib import messages
from user import models
# from django.contrib.auth.hashers import make_password , check_password
fn=''
ln=''
em=''
s=''
pswd=''
uem=''
upswd=''
conf=''
ufn=''
uln=''
ucity=''
uem=''
upswd=''
uconf=''
phone=''
# rooms table variable
p_email=''
p_type=''
p_name=''
p_adress=''
p_city=''
vacancy=''
p_monthly=''
p_facilities=''
p_img=''
datasend=''
hpass=''
hcpass=''
mohan=''
manna=''
#global variable for owner panel
ab=''
bc=''
cd=''
de=''
mystr=''
rohan=''
soham=''
ram=''
rama=''
str=''


# print(make_password('1234'))
# print(check_password('1234','pbkdf2_sha256$390000$WmWPpM1qaErlDV7lFltis5$DF5b9KSRN4OTkUy6E0XKU6Z/Klqat2TcnzB320ZLv0I='))

def home(request):
    return render(request,'home.html');

#function for owner signin
def  signin(request):
    global fn,ln,s,em,pswd,conf,phone
    if request.method=="POST": 
        d=request.POST
        for key,value in d.items():
            if key=="firstname":
                fn=value
            if key=="lastname":
                ln=value
            if key=="city":
                s=value
            if key=="email":
                em=value
            if key=="phone":
                phone=value
            if key=="password":
                pswd=value
            if key=="confpass":
                conf=value
        cursor=connection.cursor()

        cursor.execute("INSERT INTO user_owner (owner_name, owner_username,owner_email,owner_mobile,owner_passward,owner_confirmpass) VALUES('{}','{}','{}','{}','{}','{}')".format(fn,ln,em,phone,pswd,conf))
        redirect("addinfo.html")
    return render(request,"ownersignin.html") 



#function for owner login
def login(request):
    if request.method=="POST":
          oemail = request.POST.get('oemail')
          opass= request.POST.get('opass')
          
          cursor=connection.cursor()
          q="select * from user_owner where owner_email='{}' and owner_passward='{}'".format(oemail,opass)
          cursor.execute(q)
          ans=cursor.fetchall()
          res=tuple(ans)
        #   print(ans)
        #   print(res)

          if res==():
            return render(request, "ownersignin.html")
          else:
             global mohan,ab,bc,cd,de,mystr,rohan,soham,ram,rama,str
             cursor=connection.cursor()
             a="select * from user_owner,user_rooms where owner_email='{}' and p_email='{}'".format(oemail,oemail)
             cursor.execute(a)
             result=cursor.fetchall()
             ab=tuple(result)
             print(ab)

             b="select owner_name from user_owner,user_rooms where owner_email='{}' and p_email='{}'".format(oemail,oemail)
             cursor.execute(b)
             mohan=tuple(cursor.fetchall())
             for item in mohan:
                str = ''.join(item)
             bc=str
             
             
             c="select owner_email from user_owner,user_rooms where owner_email='{}' and p_email='{}'".format(oemail,oemail)
             cursor.execute(c)
             result2=cursor.fetchall()
             rohan=tuple(result2)
             for item in rohan:
                str = ''.join(item)
             cd=str

             m="select owner_mobile from user_owner,user_rooms where owner_email='{}' and p_email='{}'".format(oemail,oemail)
             cursor.execute(m)
             result2=cursor.fetchall()
             ram=tuple(result2)
             for item in ram:
                str = ''.join(item)
             rama=str


             d="select owner_username from user_owner,user_rooms where owner_email='{}' and p_email='{}'".format(oemail,oemail)
             cursor.execute(d)
             
             soham=tuple(cursor.fetchall())
             for item in soham:
                str = ''.join(item)
             de=str

             h="select vacancy from user_rooms where p_email='{}' and p_type='{}'".format(oemail,'flat')
             cursor.execute(h)
             shyam=cursor.fetchall()
             res = sum(list(map(sum, list(shyam))))

             g="select vacancy from user_rooms where p_email='{}' and p_type='{}'".format(oemail,'Room')
             cursor.execute(g)
             shyam=cursor.fetchall()
             res1 = sum(list(map(sum, list(shyam))))


             f="select vacancy from user_rooms where p_email='{}' and p_type='{}'".format(oemail,'Shop')
             cursor.execute(f)
             shyam=cursor.fetchall()
             res2 = sum(list(map(sum, list(shyam))))
             print(res)
             
             mohan={
                'ab':ab,
                'bc':bc,
                'cd':cd,
                'de':de,
                'ef':res,
                'gh':res1,
                'ij':res2,
                'rama':rama


             }
             
             
             return render(request, "ownerpanal.html",mohan)
    return render(request,"ownerlogin.html")



#function to render main login page
def mainlogin(request):
        return render(request, "loginmain.html")
             


# # Create your views here.

#functon for the user signin
def user_signin(request):
      global ufn,uln,ucity,uem,upswd,uconf,hpass
      if request.method=="POST": 
        d=request.POST
        for key,value in d.items():
            if key=="ufirstname":
                ufn=value
            if key=="ulastname":
                uln=value
            if key=="uemail":
                uem=value
            if key=="city":
                ucity=value
            if key=="upassword":
                upswd=value    
            if key=="uconf":
                uconf=value
        cursor=connection.cursor()

        cursor.execute("INSERT INTO user_user (user_name,user_username,user_email,user_city,user_passward,user_confirmpass) VALUES('{}','{}','{}','{}','{}','{}')".format(ufn,uln,uem,ucity,upswd,uconf))
        redirect("userlogin")
   
      return render(request, 'usersignin.html');

#function user login
def user_login(request):
    if request.method=="POST":
          uuemail = request.POST['uuemail']
          uupass= request.POST['uupass']
          
          cursor=connection.cursor()
          q="select * from user_user where user_email='{}' and user_passward='{}'".format(uuemail,uupass)
          cursor.execute(q)
          res=cursor.fetchall()
          tp=tuple(res)
          print(res)
          print(tp)

          if tp==():
            return render(request, "usersignin.html")
          else:
             return render(request, "index.html")

    return render(request,"userlogin.html")


#function for the contact
def contact(request):
    global name,email,msg
    
    messages.success(request,"Successfully logined.")
    if request.method=="POST": 
        d=request.POST
        for key,value in d.items():
            if key=="name":
                name=value
            if key=="email":
                email=value
            if key=="msg":
                msg=value
            
        cursor=connection.cursor()

        cursor.execute("INSERT INTO user_contact (c_name,c_email,c_msg) VALUES('{}','{}','{}')".format(name,email,msg))
   
    return render(request, 'contact.html');



def about(request):
    return render(request, 'about.html');


def addinfo(request):
     global p_type,p_name,p_adress,p_city,vacancy,p_monthly,p_facilities,p_img,p_email

     if request.method=="POST": 
        d=request.POST
        for key,value in d.items():
            if key=="ptype":
                p_type=value
            if key=="pname":
                p_name=value
            if key=="padress":
                p_adress=value
            if key=="pcity":
                p_city=value
            if key=="vacancy":
                vacancy=value
            if key=="monthly":
                p_monthly=value
            if key=="oemail":
                p_email=value
            if key=="facilities":
                p_facilities=value
            if key=="pimg":
                p_img=value 
        cursor=connection.cursor()

        cursor.execute("INSERT INTO user_rooms (p_type,p_name,p_adress,p_city,vacancy,p_monthly,p_email,p_facilities,p_img) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(p_type,p_name,p_adress,p_city,vacancy,p_monthly,p_email,p_facilities,p_img))
        

     return render(request, 'addinfo.html')

def explore(request):
     global datasend,data,p_city,p_type,p_monthly
    #  cursor=connection.cursor()
    #  m="select * from user_rooms"
    #  cursor.execute(m)
    #  ans=tuple(cursor.fetchall())
     
     data={
         
      }
    #  print(data)

     if request.method=="POST":
         hs= request.POST.get('ptype')
         ms= request.POST.get('pcity')
         ds= request.POST.get('pmoney')
         cursor=connection.cursor()
         if hs=="None" and ms=="None":
            m="select * from user_rooms where p_monthly='{}' ".format(ds)
         elif hs=="None" and ds=="None":
            m="select * from user_rooms where p_city='{}' ".format(ms)
         elif ms=="None" and ds=="None":
            m="select * from user_rooms where p_type='{}' ".format(hs)
         elif ms=="None" :
            m="select * from user_rooms where p_type='{}' AND p_monthly='{}' ".format(hs,ds)
         elif  ds=="None":
            m="select * from user_rooms where p_type='{}' AND p_city='{}'".format(hs,ms)
         elif hs=="None":
            m="select * from user_rooms where p_city='{}' AND p_monthly='{}'".format(ms,ds)
         else:
            m="select * from user_rooms where p_type='{}' AND p_city='{}' AND p_monthly='{}' ".format(hs,ms,ds)
         cursor.execute(m)
         ans=tuple(cursor.fetchall())

         data={
          'servicedata':ans
          }


         print(ans)
     return render(request, "explore.html",data)
    #  if request.method=="POST":
    #       p_type = request.POST.get('senddata')
    
    #       cursor=connection.cursor()
    #       q="select * from user_rooms where p_type='{}'".format(p_type)
    #       cursor.execute(q)
    #       ans=cursor.fetchall()
     
        
        #   res=tuple(ans)
        # #   print(ans)
        #   print(res)

        #   if res==():
        #     return render(request, "ownersignin.html")
        #   else:
        #      return redirect("addinfo/")


def infoadd(request):
    
     return render(request, 'ownermain.html');

# def login(request):
#     return render(request, 'loginmain.html');
