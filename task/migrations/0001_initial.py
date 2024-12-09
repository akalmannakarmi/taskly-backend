# Generated by Django 5.1.4 on 2024-12-09 04:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('priority', models.IntegerField(choices=[(-2, 'Lowest'), (-1, 'Low'), (0, 'Normal'), (1, 'High'), (2, 'Highest')], default=0)),
                ('points', models.IntegerField(default=0)),
                ('progress', models.IntegerField(default=0)),
                ('status', models.IntegerField(choices=[(0, 'Pending'), (1, 'Active'), (2, 'On-Hold'), (3, 'Complete')], default=0)),
                ('start_date', models.DateField(null=True)),
                ('deadline_date', models.DateField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
