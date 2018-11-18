from django.shortcuts import render

# Create your views here.
def showIndex(request):
    return render(request,"index.html")


def display(request):
    lang = request.POST.getlist("cb")
    return render(request,"index.html",{"items":lang})



