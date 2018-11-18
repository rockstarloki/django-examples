from django.shortcuts import render
from django.views.generic import View


class CheckMode(View):
    def post(self,request):
        mess ="I am post"
        return render(request,"index.html",{"message1":mess})

    def get(self,request):
        mess = "I am get"
        return render(request, "index.html", {"message2": mess})


