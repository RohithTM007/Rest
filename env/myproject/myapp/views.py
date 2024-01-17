from django.shortcuts import render

# Create your views here.
def Restaurant(request):
    return render(request,'Restaurant.html')
def home(request):
    return render(request,'home.html' )
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
