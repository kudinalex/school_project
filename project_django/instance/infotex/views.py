from django.shortcuts import render

def infotex_home(request):
    return render(request, 'infotex/infotex_home.html')