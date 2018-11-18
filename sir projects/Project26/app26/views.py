from django.shortcuts import render
from django.views.generic import View

class IndexView(View):
    def post(self,request):
        mess = "I am Post"
        return render(request,"index.html",{"message1":mess})
    def get(self,request):
        mess = "I am Get"
        return render(request,"index.html",{"message2":mess})