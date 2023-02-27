from django.shortcuts import render

def drugie_home(request):
    return render(request, 'drugie/drugie_home.html')