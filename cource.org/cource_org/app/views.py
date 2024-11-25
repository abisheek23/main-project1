from django.shortcuts import render ,redirect
from .models import *

# Create your views here.
def home(req):

    #    data=cource.objects.all()
        return render(req,'index.html')
 