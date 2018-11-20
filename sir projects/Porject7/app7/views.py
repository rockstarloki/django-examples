from django.shortcuts import render

# Create your views here.
def showregister(request):
    return render(request,"register.html")

def register(request):
    name = request.POST.get("t1")
    age = request.POST.get("t2")
    cno = request.POST.get("t3")
    email = request.POST.get("t4")
    address = request.POST.get("t5")

    d1 = {"name":name,"age":age,"contact":cno,"emailid":email,"address":address}
    return render(request,"details.html",d1)









