from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, User, Donor, NGO, NgoProfile, DonorProfile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

# to automatically create a profile for each user

@receiver(post_save, sender=Donor)
def create_profile(sender, instance, created, **kwargs):
    if created:
        DonorProfile.objects.create(user=instance)


@receiver(post_save, sender=Donor)
def save_profile(sender, instance, **kwargs):
    instance.donorprofile.save()


@receiver(post_save, sender=NGO)
def create_profile(sender, instance, created, **kwargs):
    if created:
        NgoProfile.objects.create(user=instance)

@receiver(post_save, sender=NGO)
def save_profile(sender, instance, **kwargs):
    instance.ngoprofile.save()