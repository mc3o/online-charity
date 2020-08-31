# Generated by Django 3.1 on 2020-08-26 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('charityapp', '0001_initial'),
        ('ngo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='ngo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='charityapp.ngo'),
        ),
        migrations.AddField(
            model_name='donation',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
