from django.shortcuts import render

def sample(request):
    return render(request,"index.html")
