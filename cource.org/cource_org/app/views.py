from django.shortcuts import render ,redirect
from .models import *

# Create your views here.
def home(request):
    data = cource.objects.all()  # Query all items from the database
    context = {'data': data}
    return render(request, 'index.html', context)

# def cources(req):
#     if 'user' in req.session:
#         data=cource.objects.all()
#         return render(req,'user/user_home.html',{'cources':data})
#     else:
#         return redirect()

def about(req):
   
    return render(req, 'about.html', )

def cources(req):
    data = cource.objects.all()  # Query all items from the database
    context = {'data': data}
    return render(req, 'cource.html',context)

def view_cource(req,cid):
    data=cource.objects.get(pk=cid)
    return render(req,'view_cou.html',{'data':data})

def contact(req):
    return render (req,'contact.html')

def sendm(req):
     if req.method=='POST':
          name=req.POST['name']
          email=req.POST['email']
          message=req.POST['message']
          data=Message.objects.create(name=name,email=email,message=message)
          data.save()
          return redirect(contact)
     else:
          return render(req,'contact.html')