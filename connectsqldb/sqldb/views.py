from django.shortcuts import render
from .models import Mydb

def index(request):
    return render(request,"price.html")



def save(request):
        no = request.POST.get("t1")
        name = request.POST.get("t2")
        price = request.POST.get("t3")

        db = Mydb(no=no,name=name,price=price)
        db.save()
        return render(request,"price.html")

