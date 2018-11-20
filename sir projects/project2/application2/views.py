from django.http import HttpResponse

def show(request):
    return HttpResponse("<html><body bgcolor='cyan'><center><font size=8 face='Arial Black'>Sathya Tech</font></center></body></html>")