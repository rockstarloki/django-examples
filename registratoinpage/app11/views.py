from django.shortcuts import render

def register(request):
    return render(request,"register.html")

def show(request):
    name = request.POST.get("t1")
    age = request.POST.get("t2")
    contact = request.POST.get("t3")
    email = request.POST.get("t4")
    address = request.POST.get("t5")

    f = open("sample1.txt","a")
    s=f.write("\n\nname--"+name+"\nage--"+age+"\ncontact--"+contact+"\nemail--"+email+"\naddress--"+address)
    f.close()
    d1={"name":name,"age":age,"contact":contact,"email":email,"address":address}

    return render(request,"details.html",d1)
def save(request):
    return render(request,"register.html")


