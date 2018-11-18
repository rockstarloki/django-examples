from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")


def show(request):
    movie = request.POST.getlist("cb")

    return render(request,"showimages.html",{"items":movie})
