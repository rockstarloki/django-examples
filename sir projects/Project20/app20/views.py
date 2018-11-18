from django.shortcuts import render

# Create your views here.
def showIndex(request):
    return render(request,"index.html")


def displayOne(request):
    langs = request.POST.get("lang")
    if langs == "Select":
        langs = "Please Select One Option"

    return render(request,"index.html",{"message1":langs})


def displayTwo(request):
    langs = request.POST.get("lang")
    return render(request, "index.html", {"message2": langs})


def displayThree(request):
    langs = request.POST.getlist("lang")
    return render(request, "index.html", {"message3": langs})











