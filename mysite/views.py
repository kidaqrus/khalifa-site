from django.shortcuts import render
from django.conf import settings


# Create your views here.
def post_list(request):
    return render(request, 'mysite/index.html')