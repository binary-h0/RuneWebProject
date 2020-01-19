from django.shortcuts import render
from django.http import HttpResponse

#from .models import

# Create your views here.
def main(request):
    return render(request, 'rune_web/main.html')

def cardinfo(request):
    return render(request,"rune_web/cardinfo.html")

def deckbuilder(request):
    return render(request,"rune_web/deckbuilder.html")

def community(request):
    return render(request,"rune_web/community.html")
