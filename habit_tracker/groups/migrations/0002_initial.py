# Generated by Django 5.1.5 on 2025-01-27 18:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goals', '0002_initial'),
        ('groups', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='groupmembership',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sharedgoal',
            name='goal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goals.goal'),
        ),
        migrations.AddField(
            model_name='sharedgoal',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.accountabilitygroup'),
        ),
    ]
