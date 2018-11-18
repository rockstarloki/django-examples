from django.shortcuts import render

def one(request):

    return render(request,"one.html")

def two(request):
    global name
    name = request.POST.get("t1")

    return render(request,"two.html")

def three(request):
    global age
    age = request.POST.get("t2")

    return render(request,"three.html")

def all(request):
    address = request.POST.get("t3")
    d1 = {"name": name ,"age": age ,"address": address}
    return render(request,"one.html",d1)


