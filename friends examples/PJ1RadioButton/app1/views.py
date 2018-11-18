from django.shortcuts import render


def show(request):
    return render(request,"index.html")


def displayOne(request):
    langs = request.POST.get("lang")
    return render(request,"index.html",{"language":langs})


def displayTwo(request):
    langs=request.POST.get("lang")
    if langs == "select":
        lang = "Please select in one language"
        return render(request,"index.html",{"language3":lang})

    return render(request,"index.html",{"language2":langs})


def displayThree(request):
    langs = request.POST.getlist("lang")

    return render(request,"index.html",{"language4":langs})