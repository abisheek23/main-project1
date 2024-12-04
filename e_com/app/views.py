from django.shortcuts import render,redirect

from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import *
import os
from django.contrib.auth.models import  User
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
3

def e_com_login(req):
    if 'shop' in req.session:
        return redirect(shop_home)
    if 'user' in req.session:
        return redirect (user_home)
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['password']
        data=authenticate(username=uname,password=password)
        if data:
            login(req,data)
            if data.is_superuser:
              req.session['shop']=uname   #create session 
              return redirect(shop_home)
            else:
                req.session['user']=uname
                return redirect(user_home)
        else:
            messages.warning(req, " invalid user name or password")
            return redirect(e_com_login)
    else:
        return render(req,'login.html')
def e_com_logout(req):
    logout(req)
    req.session.flush()
    return redirect(e_com_login)
        

def shop_home(req):
    if 'shop' in req.session:
       data=prodect.objects.all()
       return render(req,'shop/home.html',{'products':data})
    else:
        return redirect(e_com_login)


def add_product(req):
    if 'shop' in req.session:
        if req.method=='POST':
            pid=req.POST['pid']
            name=req.POST['name']
            dis=req.POST['description']
            price=req.POST['price']
            offer_price=req.POST['off_price']
            stock=req.POST['stock']
            file=req.FILES['image']
            data=prodect.objects.create(pid=pid,name=name,dis=dis,price=price,offer_price=offer_price, stoct=stock,img=file)

            data.save()
            return redirect (shop_home)
        else:
            return render(req,'shop/add_product.html')
    else:
        return redirect(e_com_login)

def edit_product(req,pid):
    if req.method=='POST':
        p_id=req.POST['pid']
        name=req.POST['name']
        dis=req.POST['description']
        price=req.POST['price']
        offer_price=req.POST['off_price']
        stock=req.POST['stock']
        file=req.FILES.get('image')
        if file:
            prodect.objects.filter(pk=pid).update(pid=p_id,name=name,dis=dis,price=price,offer_price=offer_price,stoct=stock)
            data=prodect.objects.get(pk=pid)
            data.img=file
            data.save()
        else:
            prodect.objects.filter(pk=pid).update(pid=p_id,name=name,dis=dis,price=price,offer_price=offer_price,stoct=stock)
        return redirect(shop_home)

    else:
        data=prodect.objects.get(pk=pid)
        return  render(req,'shop/edit.html',{'data':data})

def delet_product(req,pid):
    data=prodect.objects.get(pk=pid)
    file=data.img.url
    file=file.split('/')[-1]
    os.remove('media/'+file)
    data.delete()
    return redirect(shop_home)

def register(req):
    if req.method=='POST':
        uname=req.POST['uname']
        email=req.POST['email']
        pswd=req.POST['pswd']
        print(email)
        send_mail('account created', 'you created a account in e_com', settings.EMAIL_HOST_USER, [email])

        try:
          data=User.objects.create_user(first_name=uname, username=email,email=email,password=pswd)
          data.save()
          return redirect (req,e_com_login)
        except:
           messages.warning(req, " already used ")
           return redirect(register)
    else:
        return render(req,'user/registration.html')

def user_home(req):
    if 'user' in req.session:
        data=prodect.objects.all()
        return render(req,'user/user_home.html',{'products':data})
    else:
        return redirect(e_com_login)
    
def view_pro(req,pid):
    data=prodect.objects.get(pk=pid)
    return render(req,'user/viewpro.html',{'product':data})

def add_to_cart(req,pid):
    product=prodect.objects.get(pk=pid)
    user=User.objects.get(username=req.session['user'])
    try:
        data=Cart.objects.get(product=product,user=user)
        data.qty+=1
        data.save()
    except:
        data=Cart.objects.create(product=product,user=user,qty=1)
        data.save()
    return redirect(view_cart)

def view_cart(req):
    user=User.objects.get(username=req.session['user'])
    data=Cart.objects.filter(user=user)

    return render (req,'user/cart.html',{'cart':data})

def qty_in(req,cid):
    data=Cart.objects.get(pk=cid)
    data.qty+=1
    data.save()
    return redirect(view_cart)

def cart_buy(req,cid):
    cart=Cart.objects.get(pk=cid)
    prodect=cart.product
    user=cart.user
    qty=cart.qty
    price=prodect.offer_price*qty
    buy=buy.objects.create(prodect=prodect,user=user,qty=qty,price=price)
    buy.save()
    return redirect(bookings)

def buybuy(req,pid):

    product=prodect.objects.get(pk=pid)
    user=User.objects.get(username=req.session['user'])
    qty=1
    price=product.offer_price
    buy=Buy.objects.create(product=product,user=user,qty=qty,price=price)
    buy.save()
    return redirect(bookings)

def bookings(req):
    user=User.objects.get(username=req.session['user'])
    buy=Buy.objects.filter(user=user)[::-1]

    return render(req,'user/book.html',{'bookings':buy})




def view_bookings(req):
    buy=Buy.objects.all()[::-1]
    return redirect (req,'user/home')
