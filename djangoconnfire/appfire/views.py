from django.shortcuts import render
from firebase.firebase import FirebaseApplication

def register(request):
    pno = request.POST.get("t1")
    fire = FirebaseApplication("https://mydemo-820c3.firebaseio.com/", None)
    d1 = fire.get("myproduct",pno)

    return render(request,"index.html",{"data":d1})

def save(request):
    pno = request.POST.get("t1")
    pname = request.POST.get("t2")
    pprice = request.POST.get("t3")
    fire = FirebaseApplication("https://mydemo-820c3.firebaseio.com/",None)
    p = fire.put("myproduct",pno,{"pname":pname,"pprice":pprice,})
    d = fire.get("myproduct",None)
    return render(request,"index.html",{"data":d})

def show(request):
    pno = request.POST.get("t1")
    pname = request.POST.get("t2")
    pprice = request.POST.get("t3")
    fire = FirebaseApplication("https://mydemo-820c3.firebaseio.com/", None)
    d1 = fire.get("myproduct", pno, {"pname": pname, "pprice": pprice})

    return render(request, "index.html",d1)

def delete(request):
    pno = request.POST.get("t1")
    print(pno)
    fire = FirebaseApplication("https://mydemo-820c3.firebaseio.com/",None)
    fire.delete("myproduct",pno)
    d = fire.get("myproduct/",None)

    return render(request,"index.html",{"data":d})

def update(request):
    pno = request.GET.get("id")
    fire = FirebaseApplication("https://mydemo-820c3.firebaseio.com/", None)
    d = fire.get("myproduct/", pno)
    d1 = fire.get("myproduct/",None)

    return render(request, "index.html", {"d1": d,"d":pno,"data":d1})
