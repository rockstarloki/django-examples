
from django.shortcuts import render

def showIndex(request):
    response = render(request,"one.html")
    response.set_cookie(key="name",value="Sathya Tech")
    response.set_cookie(key="lang",value="Python Naveen")
    return response


def showCookie(request):
    name = request.COOKIES["name"]
    lang = request.COOKIES["lang"]
    result = name+"---"+lang
    return render(request,"one.html",{"c_name":result})