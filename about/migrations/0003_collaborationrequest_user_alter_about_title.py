# Generated by Django 4.2.18 on 2025-01-20 01:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('about', '0002_collaborationrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='collaborationrequest',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='collaboration_requests', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='about',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
