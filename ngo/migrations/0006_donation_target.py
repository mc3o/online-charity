# Generated by Django 3.1 on 2020-09-02 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0005_auto_20200827_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='target',
            field=models.CharField(default=0, max_length=100, null=True),
        ),
    ]
