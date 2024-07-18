from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,"core/index.html")

#view|controller for contact page
def contact(request):
    return render(request,"core/contact.html")