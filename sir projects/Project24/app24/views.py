from django.shortcuts import render


def showIndex(request):
    return render(request,"index.html")

def checkMethod(request):
    if request.method == "POST":
        mess = "I am From Post"
        return render(request, "index.html", {"message1": mess})
    else:
        mess = "I am From Get"
        return render(request, "index.html", {"message2": mess})


