from django.shortcuts import render
from django.views.generic import View


class Payment(View):
    def post(self,request):
        list_items = request.POST.getlist("p1")
        if list_items == []:
            return render(request,"products.html",{"error":"Please Select One or More Item's"})
        else:
            print(list_items)
            return render(request,"products.html")


class LoginCheck(View):
    def post(self,request):
        uname = request.POST.get("uname")
        upass = request.POST.get("upass")

        if uname == "sathya" and upass == "tech":
            pass
        else:
            pass
