# views.py
from django.shortcuts import render

def unity_game(request):
    return render(request, 'unity.html')
