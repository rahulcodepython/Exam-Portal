# Generated by Django 4.0 on 2022-03-07 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_remove_custom_user_avg_remove_custom_user_total'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Examinee',
        ),
    ]