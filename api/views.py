 
from django.shortcuts import render,HttpResponse
import pyjokes
from django.http import JsonResponse
# Create your views here.
 
def home(request):
    joke=pyjokes.get_joke()
    return render(request,"main/index.html",{"joke":joke})


def get_new_joke(request):
    new_joke = pyjokes.get_joke()
    return JsonResponse({"joke": new_joke})
