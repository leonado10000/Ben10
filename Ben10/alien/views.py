from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
k = [ 
    "https://static.wikia.nocookie.net/ben10/images/3/38/OV_AlienX.png/revision/latest?cb=20200518024327" ,
    "https://static.wikia.nocookie.net/chainsaw-man/images/d/d9/Makima_anime_design_2.png/",
    "https://static.wikia.nocookie.net/thebate/images/7/76/Disciplinary_Committee_Arthur.png",
    "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/561726f8-9610-4a0f-8481-652e94fc6a7c/ddwgto0-01407ebc-ba37-45ee-a72d-f2e62b28be73.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzU2MTcyNmY4LTk2MTAtNGEwZi04NDgxLTY1MmU5NGZjNmE3Y1wvZGR3Z3RvMC0wMTQwN2ViYy1iYTM3LTQ1ZWUtYTcyZC1mMmU2MmIyOGJlNzMucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.rMgnbJ6bAL2egGzi6Obq41G2FwsR1S1Qlhy4bKNwJtk",
    "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/e0516fda-e907-4a96-b968-333a26dcd26c/d3jb44d-987c343f-f3ef-411c-9fee-1f419bb9ab6b.png/v1/fill/w_900,h_2333,strp/kakashi_png_by_hidan_sama1408_d3jb44d-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MjMzMyIsInBhdGgiOiJcL2ZcL2UwNTE2ZmRhLWU5MDctNGE5Ni1iOTY4LTMzM2EyNmRjZDI2Y1wvZDNqYjQ0ZC05ODdjMzQzZi1mM2VmLTQxMWMtOWZlZS0xZjQxOWJiOWFiNmIucG5nIiwid2lkdGgiOiI8PTkwMCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.gcTuyHhLfVU8mvbuUeRajtFy7jSz3gQR-8WSeRGi4vo"
]
cont = ["Alien X","makima","Arthur","Sung jin woo","Kakashi"]
def index(request):
    try:
        return render(request, "alien/index.html" , {
            "aliens":k,"cont":cont
        })
    except:
        return HttpResponse("heello world")