from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone


# Create your views here.
def index(request):
    return render(request, 'VerbNet/index.html', {})

def verbs(request):
  return render(request, 'VerbNet/verbs.html', {})