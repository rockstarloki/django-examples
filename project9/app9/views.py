from django.shortcuts import render
# To show register page
def login(request):
    return render(request,"login.html")

# To read the data and send in to the next  page
def details(request):
    name =request.POST.get("t1")
    age = request.POST.get("t2")
    cno = request.POST.get("t3")
    email = request.POST.get("t4")
    address = request.POST.get("t5")
    d1 = {"name":name,"age":age,"cno":cno,"email":email,"address":address}
    return render(request,"details.html",d1)
