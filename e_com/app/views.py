from django.shortcuts import render,redirect

from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import *
import os
# Create your views here.
3

def e_com_login(req):
    if 'shop' in req.session:
        return redirect(shop_home)
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['password']
        data=authenticate(username=uname,password=password)
        if data:
            login(req,data)
            req.session['shop']=uname   #create session 
            return redirect(shop_home)
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
    # os.remove('media/'+file)
    data.delete()
    return redirect(shop_home)