# Generated by Django 3.1 on 2020-08-27 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('charityapp', '0001_initial'),
        ('ngo', '0004_madedonation_ngo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='madedonation',
            name='user',
        ),
        migrations.AddField(
            model_name='madedonation',
            name='donor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='charityapp.donor'),
        ),
    ]
