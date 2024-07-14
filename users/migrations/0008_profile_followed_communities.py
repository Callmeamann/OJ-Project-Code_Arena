# Generated by Django 5.0.6 on 2024-07-11 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_delete_followrequest'),
        ('users', '0007_delete_contest'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='followed_communities',
            field=models.ManyToManyField(blank=True, related_name='followers', to='community.community'),
        ),
    ]