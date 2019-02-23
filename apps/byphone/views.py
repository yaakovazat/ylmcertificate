from django.shortcuts import render

# Create your views here.
def phone(request):
    return render(request,'byphone.html')