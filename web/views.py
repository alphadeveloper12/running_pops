from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Wallet, CheckBenefit
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

def benefits(request):
    return render(request, 'benefits.html')

def benefits_form(request):
    if request.method == 'POST':
        data = request.POST  # Use request.POST (uppercase) to access the POST data
        benefit = CheckBenefit(wallet_address=data['wallet_address'],nft_number=data['nft_number'],twitter_handle=data['twitter_handler'],nft_link_url=data['nft_link'],collection_name=data['collection_name'],message=data['message'])
        try:
            benefit.save()
            messages.success(request, 'your details got submitted, now our team will start the process transforming your 2D pfp into a 3D pfp, you will get notified by email once its done to claim it.')
            return redirect('benefits_form')
        except ValidationError as e:
            messages.error(request, f"Error adding benefit: {e}")
            return render(request, 'benefit_form.html')

        return redirect('benefits_form')
    else:
        return render(request, 'benefit_form.html')
def submit_wallet(request):
    if request.method == 'POST':
        data = request.POST  # Use request.POST (uppercase) to access the POST data
        wallet = Wallet(wallet_address=data['wallet'])
        try:
            wallet.save()
            messages.success(request, 'Wallet added successfully.')
            return redirect('whitelist')
        except ValidationError as e:
            messages.error(request, f"Error adding wallet: {e}")
            return render(request, 'whitelist.html')

        return redirect('whitelist')
    else:
        return render(request, 'whitelist.html')

