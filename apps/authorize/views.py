from django.shortcuts import render

# Create your views here.
def authorize(request):
    return render(request,'authorize.html')