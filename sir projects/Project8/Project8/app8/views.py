from django.shortcuts import render

def showIndex(request):
    return render(request,"index.html")

def display(request):
    name = request.POST.get("t1")
    cno = request.POST.get("t2")
    d1 = {"k1":name,"k2":cno}
    return render(request,"details.html",d1)


def saveDetails(request):
    name = request.POST.get("t1")
    cno = request.POST.get("t2")
    text = "Name : "+name+"\nContact No : "+cno+"\n --------------------\n"
    f = open("Details.txt","a")
    f.write(text)
    f.close()
    return render(request,"index.html")