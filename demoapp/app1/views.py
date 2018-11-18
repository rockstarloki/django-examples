from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,"login.html")
def validate(request):
    name = request.POST.get("t1")
    age = request.POST.get("t2")
    cno = request.POST.get("t3")
    email = request.POST.get("t4")
    password = request.POST.get("t5")
    return render(request,"details.html")
def details(request):
    name = request.POST.get("t1")
    age = request.POST.get("t2")
    cno = request.POST.get("t3")
    email = request.POST.get("t4")
    password = request.POST.get("t5")

    f = open("sample.txt","a")
    f.write("name :"+name+"\nage :"+age+"\ncno:" +cno+"\nemail :"+email+"\npassword :"+password+"\n------------\n")
    f.close()
    return render(request,"login.html")

