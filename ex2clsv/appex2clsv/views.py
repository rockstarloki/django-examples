from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Data

def index(request):
    request.session["status"] = False
    return render(request,"index.html")

#validating select product and create session and also login
def product(request):
    pros = request.POST.getlist("t1")
    status = request.session["status"]
    if pros == []:
        return render(request,"product.html",{"mess":"please select a product"})
    else:
        if status :
            request.session["status"] = True
            return redirect("/payment/")
        else:
            return redirect("/login/")

#getting the data from db and checking login
class Logincheck(View):
    def post(self,request):
        uname = request.POST.get("username")
        upass = request.POST.get("password")
        f = Data.objects.filter(username=uname,password=upass)
        if f.count() == 0:
            return render(request,"registration.html",{"miss":"please register and login"})
        else:
            request.session["status"] = True
            return redirect("/product/")

#creating user and saving to database
def Registration(request):
    idno = request.POST.get("idno")
    name = request.POST.get("name")
    contact = request.POST.get("contact")
    uname = request.POST.get("username")
    upass = request.POST.get("password")

    s = Data(idno=idno,name=name,contact=contact,username=uname,password=upass)
    s.save()

    return render(request,"registration.html",{"mes":"successfully registered"})


def payment(request):
    return render(request,"payment.html")
