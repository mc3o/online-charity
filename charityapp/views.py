from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import (SignUpForm, UserUpdateForm, ProfileUpdateForm,
                    NgoSignUpForm, DonorSignupForm, NgoUpdateForm,
                    DonorUpdateForm)

from django.contrib.auth.decorators import login_required
from .emails import send_welcome_email
from .decorators import donor_required, ngo_required
from django.views.generic import CreateView
from .models import User, Donor, NGO
from ngo.models import MadeDonation, Donation, Category


# Create your views here.
def index(request):
    return render(request, 'users/welcome.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            user = authenticate(username=username, password=raw_password)
            messages.success(request, f'Account created')
            send_welcome_email(username, email)
            login(request, user)
            return redirect('welcome')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})


@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        up_form = UserUpdateForm(request.POST, instance=request.user)
        pr_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if up_form.is_valid() and pr_form.is_valid():
            up_form.save()
            pr_form.save()
            messages.success(request, f'Account has been updated')
            return redirect('profile')
    else:
        up_form = UserUpdateForm(instance=request.user)
        pr_form = ProfileUpdateForm(instance=request.user.profile)
    content = {
        'user_form': up_form,
        'profile_form': pr_form,
    }
    return render(request, 'users/profile.html', content)


class DonorSignUpView(CreateView):
    model = User
    form_class = DonorSignupForm
    template_name = 'users/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'donor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        image = form.cleaned_data.get('image')
        messages.success(self.request, f'Account created')
        send_welcome_email(username, email)

        return redirect('welcome')


class NgoSignUpView(CreateView):
    model = User
    form_class = NgoSignUpForm
    template_name = 'users/ngo_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'ngo'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, f'Account created')
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        send_welcome_email(username, email)

        return redirect('welcome')


@donor_required
def donor_profile(request):
    user = request.user
    donor_pr = Donor.objects.filter(pk=user).first()
    donations_made = MadeDonation.objects.filter(donor_id=donor_pr)
    print(donations_made)
    if request.method == 'POST':
        pr_form = DonorUpdateForm(request.POST, request.FILES, instance=donor_pr)
        if pr_form.is_valid():
            pr_form.save()
            messages.success(request, f'Account has been updated')
            return redirect('donor_profile')
    else:
        pr_form = DonorUpdateForm(instance=donor_pr)
    content = {
        'donor': donor_pr,
        'profile_form': pr_form,
        'donations': donations_made
    }
    return render(request, 'users/donor_profile.html', content)


@ngo_required
def ngo_profile(request):
    user = request.user
    ngo_pr = NGO.objects.filter(pk=user).first()
    donations_received = MadeDonation.objects.filter(ngo_id=ngo_pr)
    print(donations_received)
    if request.method == 'POST':
        pr_form = NgoUpdateForm(request.POST, request.FILES, instance=ngo_pr)
        if pr_form.is_valid():
            pr_form.save()
            messages.success(request, f'Account has been updated')
            return redirect('ngo_profile')
    else:
        pr_form = NgoUpdateForm(instance=ngo_pr)
    content = {
        'ngo': ngo_pr,
        'profile_form': pr_form,
        'donations': donations_received
    }
    return render(request, 'users/ngo_profile.html', content)


@login_required
def search_donations(request):
    if 'search_donations' in request.GET:
        name = request.GET.get("search_donations")
        cat_id = Category.objects.filter(name=name).first()

        donation_req = Donation.objects.filter(category=cat_id).order_by('-pub_date')
        # print(donation_req)
        approved_donations = []
        for donation in donation_req:
            if donation.status == True:
                approved_donations.append(donation)
        print(approved_donations)
        message = f'name'
        params = {
            'results': approved_donations,
            'name':name

        }
        return render(request, 'users/results.html', params)
    else:
        message = "You haven't searched for any donations"
    return render(request, 'users/results.html', {'message': message})
