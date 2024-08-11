from django.shortcuts import render


def home(request):
    return render(request, 'MovieReviews/home.html')



def contact(request):
    return render(request, 'MovieReviews/contact.html')



def index(request):
    return render(request, 'AppBuilder9000/Home/index.html')

