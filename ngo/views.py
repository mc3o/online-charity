from django.shortcuts import render, redirect, get_object_or_404, reverse
from .forms import DonationForm, RequestForm, CategoryForm
from django.http import HttpResponseRedirect, JsonResponse
from .models import Donation, MadeDonation, Category
from django.contrib.auth.decorators import login_required
from charityapp.decorators import ngo_required, donor_required
from charityapp.models import NGO, Donor
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic.edit import FormMixin



# Create your views here.


def welcome(request):
    donations = Donation.objects.order_by('-pub_date')
    categories = Category.objects.all()

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
        'categories': categories,
    }
    return render(request, 'welcome.html', context)

@method_decorator(login_required, name='dispatch')
class DonationDetailDonorView(FormMixin, DetailView):
    model = Donation
    template_name = 'ngo/donation_donor_detail.html'
    form_class = DonationForm

    def get_success_url(self):
        return reverse('donation_donor_detail', kwargs={'pk': self.object.id})


    def get_context_data(self, **kwargs):
        context = super(DonationDetailDonorView, self).get_context_data(**kwargs)
        made_donations = MadeDonation.objects.filter(donation=self.object.id)
        remaing_amm = 0
        amm_donated = 0
        for donation in made_donations:
            amm_donated += int(donation.amount)

        print(amm_donated)
        remaing_amm = (int(self.object.target) - amm_donated)

        context['donations'] = made_donations
        context['amt_remaining'] = remaing_amm
        context['form'] = DonationForm(initial={'donation': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        print(self.object.id)
        donation = Donation.objects.filter(id=self.object.id).first()
        donor = Donor.objects.filter(name=self.request.user).first()
        form.instance.donor = donor
        form.instance.donation = donation
        form.instance.ngo = donation.ngo
              
        form.save()
        
        return super(DonationDetailDonorView, self).form_valid(form)

class DonationDetailView(DetailView):
    model = Donation
    template_name = 'ngo/donation_detail.html'

    def get_context_data(self, **kwargs):
        context = super(DonationDetailView, self).get_context_data(**kwargs)
        made_donations = MadeDonation.objects.filter(donation=self.object.id)
        remaing_amm = 0
        amm_donated = 0
        for donation in made_donations:
            amm_donated += int(donation.amount)

        remaing_amm = (int(self.object.target) - amm_donated)

        context['donations'] = made_donations
        context['amt_remaining'] = remaing_amm
        return context  



@method_decorator(login_required, name='dispatch')
class DonationUpdateView(UpdateView):
    model = Donation
    fields = ['name', 'description', 'target']

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
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Category successfully added')
            return redirect('admin_profile')
    form = CategoryForm()
    donation_req = Donation.display_all_donations()
    app_donations = []
    rej_donations = []
    for donation in donation_req:
        if donation.status == True:
            app_donations.append(donation)
        else:
            rej_donations.append(donation)
    categories = Category.objects.all()
    donors = Donor.objects.all()
    ngos = NGO.objects.all()
    context = {
        'donations': donation_req,
        'categories': categories,
        'app_donations': app_donations,
        'rej_donations': rej_donations,
        "form": form,
        "donors": donors,
        "ngos": ngos
    }
    return render(request, 'admin_profile.html', context)

@user_passes_test(lambda u: u.is_superuser)
def delete_category(request, id):
    category = Category.objects.filter(id=id)
    category.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@ngo_required
def request_donation(request):
    user = request.user
    ngo = NGO.objects.filter(name=user).first()
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            don = form.save(commit=False)
            don.ngo = ngo
            don.save()

            return HttpResponseRedirect('/')

    else:
        form = RequestForm()
        return render(request, 'request-form.html', {"form": form})


@login_required
def approve_request(request, id):
    donation = Donation.objects.filter(id=id).first()
    print(donation)
    donation.status = True
    donation.save()
    messages.success(request, f'Request approved')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@donor_required
def make_donation(request, id):
    donation = Donation.objects.filter(id=id).first()
    donor = Donor.objects.filter(name=request.user).first()
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            don = form.save(commit=False)
            # print(Donor.objects.filter(name=request.user))
            don.donor = donor
            don.donation = donation
            don.ngo = donation.ngo
            don.save()

            return HttpResponseRedirect('/')

    else:
        form = DonationForm()
        context = {
            'form': form,
            'donation': donation
        }
        return render(request, 'donationforms.html', context)


@user_passes_test(lambda u: u.is_superuser)
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Category successfully added')
            return redirect('admin_profile')
    else:
        form = CategoryForm()
        return render(request, 'category_form.html', {"form": form})
