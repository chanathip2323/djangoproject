from django.shortcuts import render
from .models import Post
#import json
#import request
# Create your views here.
def hello(request):
    #เเสดงข้อมูลจากโมเดล
    data = Post.objects.all()
    return render(request,'index.html',{'posts': data})

def page1(request):
    return render(request,'page1.html')

def createForm(request):
    return render(request,'form.html')

def addBlog(request):
    name = request.POST['name']
    desc = request.POST['desc']
    print(name,desc)
    data = Post.objects.all()
    return render(request,'index.html',{'posts': data,'name':name, 'desc':desc})

