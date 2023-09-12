from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import NFTWalletForm
from django.contrib import messages
# Create your views here.


def home(request):
    return render(request, 'index.html')


def whitelist(request):
    return render(request, 'whitelist.html')

def about(request):
    return render(request, 'about.html')

def action(request):
    return render(request, 'action.html')

def tournament(request):
    return render(request, 'tournament.html')
def submit_wallet(request):
    if request.method == 'POST':
        data = request.POST  # Use request.POST (uppercase) to access the POST data
        wallet = NFTWalletForm(wallet_address=data['wallet'])
        try:
            wallet.save()
            print('wdeer')
            messages.success(request, 'Wallet added successfully.')
            return redirect('whitelist')
        except ValidationError as e:
            messages.error(request, f"Error adding wallet: {e}")
            return render(request, 'whitelist.html')

        return redirect('whitelist')
    else:
        return render(request, 'whitelist.html')
