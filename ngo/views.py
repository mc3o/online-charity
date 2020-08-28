from django.shortcuts import render, redirect, get_object_or_404
from .forms import DonationForm, RequestForm
from django.http import HttpResponseRedirect, JsonResponse
from .models import Donation, MadeDonation
from django.contrib.auth.decorators import login_required
from charityapp.decorators import ngo_required, donor_required
from charityapp.models import NGO
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

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

class DonationDetailView(DetailView):
    model = Donation

def donations_detail(request, id):
    donation = Donation.objects.filter(id=id).first()
    context = {
        'donation': donation,
    }
    return render(request, 'donation-detail.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_profile(request):
    donation_req = Donation.display_all_donations()
    context = {
        'donations': donation_req,
    }
    return render(request, 'admin_profile.html', context)

# def Donations(request):
#     if request.method == 'POST':
#        form = DonationsForm(request.POSTFILES)
#        if form.is_valid():
#            donations = form.save(commit=False)
#            donations.save()
#            #return redirect (home)
#            return HttpResponseRedirect('/')

#     else:
#         form = DonationsForm()
#         return render(request, 'donationforms.html', {"form": form})

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


@donor_required
def make_donation(request, id):
    donation = Donation.objects.filter(id=id).first()
    
    if request.method == 'POST':
        form = DonationForm(request.POST)   
        if form.is_valid():

            don = form.save(commit=False)
            don.user=request.user
            don.donation=donation
            don.ngo=donation.ngo
            don.save()
            
            return HttpResponseRedirect('/')

    else:
        form = DonationForm()
        context = {
            'form':form,
            'donation': donation
        }
        return render(request, 'donationforms.html', context)
   


    