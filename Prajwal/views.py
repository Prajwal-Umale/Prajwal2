from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def pro(request):
    return render(request,'pro.html')

def like(request):
    return render(request,'like.html')

def con(request):
    return render(request,'contact.html')