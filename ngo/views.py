from django.shortcuts import render, redirect, get_object_or_404, reverse
from .forms import DonationForm, RequestForm
from django.http import HttpResponseRedirect, JsonResponse
from .models import Donation, MadeDonation
from django.contrib.auth.decorators import login_required
from charityapp.decorators import ngo_required, donor_required
from charityapp.models import NGO, Donor
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.

def welcome(request):
    donations = Donation.objects.all()

    app_donations = []
    rej_donations = []
    for donation in donations:
        if donation.status == True:
            app_donations.append(donation)
        else:
            rej_donations.append(donation)
    context = {
        'app_donations': app_donations,
        'rej_donations': rej_donations,        
    }
    return render(request, 'welcome.html', context)

class DonationDetailView(DetailView):
    model = Donation

@method_decorator(login_required, name='dispatch')
class DonationUpdateView(UpdateView):
    model = Donation
    fields = ['name', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        donation = self.get_object()
        if self.request.user == donation.user:
            return True
        return False


@method_decorator(login_required, name='dispatch')
class DonationDeleteView(DeleteView):
    model = Donation
    success_url = '/'

    def test_func(self):
        donation = self.get_object()
        if self.request.user == donation.user:
            return True
        return False

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

@ngo_required
def request_donation(request):
    user = request.user
    ngo = NGO.objects.filter(name=user).first()
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            don = form.save(commit=False)            
            don.ngo=ngo
            don.save()
            
            return HttpResponseRedirect('/')

    else:
        form = RequestForm()
        return render(request, 'request-form.html', {"form": form})

@login_required
def approve_request(request, id):
    donation = Donation.objects.filter(id=id).first()
    donation.status=True
    donation.save()
    return render(request, 'donation_approval.html')


@donor_required
def make_donation(request, id):
    donation = Donation.objects.filter(id=id).first()
    donor = Donor.objects.filter(name=request.user).first()
    if request.method == 'POST':
        form = DonationForm(request.POST)   
        if form.is_valid():
            don = form.save(commit=False)
            don.donor=donor
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
   


    