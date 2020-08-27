from django.shortcuts import render, redirect, get_object_or_404
from .forms import DonationsForm, RequestForm
from django.http import HttpResponseRedirect, JsonResponse
from .models import Donation
from django.contrib.auth.decorators import login_required
from charityapp.decorators import ngo_required, donor_required
from charityapp.models import NGO
# Create your views here.

def welcome(request):
    donations = Donation.objects.all()
    app_donations = []
    for donation in donations:
        if donation.status == True:
            app_donations.append(donation)
    context = {
        'donations': app_donations,
    }
    return render(request, 'welcome.html', context)

@login_required
def admin_profile(request):
    donation_req = Donation.display_all_donations()
    context = {
        'donations': donation_req,
    }
    return render(request, 'admin_profile.html', context)

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

@ngo_required
def request_donation(request):
    user = request.user
    print(user.id)
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            desc = form.cleaned_data.get('description')
            category = form.cleaned_data.get('category')
            print(category)
            donation = Donation.objects.create(
                                                name=name,
                                                description = desc,
                                                category = category,
                                                ngo_id = request.user.id,                                                
                                                )
            donation.save_donations()
            return HttpResponseRedirect('/')

    else:
        form = RequestForm()
        return render(request, 'request-form.html', {"form": form})

@login_required
def approve_request(request, id):
    donation = Donation.objects.filter(id=id).first()
    print(donation.status)
    donation.status=True
    donation.save()
    print(donation.status)
    return render(request, 'donation_approval.html')