from django.shortcuts import render


# Create your views here.
def index(request):
    myname ="son"
    return render(request, "home/index.html",{"name":myname})
