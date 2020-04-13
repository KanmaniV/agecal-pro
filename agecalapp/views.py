from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_page_view(request):
    return render(request, 'agecalapp/home.html')

def main_page_view(request):
    return render(request, 'agecalapp/mainpage.html')

def result_page_view(request):
    return render(request, 'agecalapp/resultpage.html')