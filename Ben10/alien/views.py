from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
k = [ "https://static.wikia.nocookie.net/ben10/images/3/38/OV_AlienX.png/revision/latest?cb=20200518024327" ]
cont = ["Alien X"]
def index(request):
    try:
        return render(request, "alien/index.html" , {
            "aliens":k,"cont":cont
        })
    except:
        return HttpResponse("heello world")