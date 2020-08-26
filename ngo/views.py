from django.shortcuts import render, redirect, get_object_or_404
from .forms import DonationsForm, RequestForm
from django.http import HttpResponseRedirect, JsonResponse
from .models import Donations
# Create your views here.


def Donations(request):
    if request.method == 'POST':
       form = DonationsForm(request.POST, request.FILES)
       if form.is_valid():
           donations = form.save(commit=False)
           donations.save()
           #return redirect (home)
           return HttpResponseRedirect('/')

    else:
        form = DonationsForm()
        return render(request, 'donationforms.html', {"form": form})


def Request_Donations(request):
    if request.method == 'POST':
        form = RequestForm(request.POST, request.FILES)
        if form.is_valid():
            donations_request = form.save(commit=False)
            donations_request.save()
            #return redirect (home)
            return HttpResponseRedirect('/')

    else:
            form = RequestForm()
            return render(request, 'request-form.html', {"form": form})
     
