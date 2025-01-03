# Generated by Django 5.1.4 on 2024-12-27 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0009_alter_eventssection_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookadateform',
            name='num_people',
            field=models.PositiveIntegerField(verbose_name='Number of People'),
        ),
        migrations.AlterField(
            model_name='contactsection',
            name='opening_hours',
            field=models.TextField(verbose_name='Calling Hours'),
        ),
        migrations.AlterField(
            model_name='websitedetail',
            name='logo',
            field=models.ImageField(null=True, upload_to='logo/', verbose_name='Business logo'),
        ),
    ]
