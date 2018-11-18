from django.shortcuts import render, redirect
from django.views.generic import View

def showindex(request):
    request.session["status"] = False
    return render(request,"index.html")

class Selectproduct(View):
    def post(self,request):
        products = request.POST.getlist("p1")
        status = request.session["status"]
        if products == []:
            return render(request,"product.html",{"error":"please select a product"})
        else:
            if status :
                request.session["status"] = True
                return redirect("/payment/")
            else:
                return render(request,"login.html")

def logincheck(request):
    uname = request.POST.get("t1")
    upass = request.POST.get("t2")
    if uname == "rockstar" and upass == "lokesh":
        request.session["status"] = True
        return redirect("/product/")
    else:
        mess  = "invallid username"
        return render(request,"login.html",{"mess":mess})


def payment(request):
    return render(request,"payment.html")
