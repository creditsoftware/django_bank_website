# Generated by Django 2.1.5 on 2020-08-21 14:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0011_auto_20200821_1529'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now=True, null=True)),
                ('loan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='frontend.Loan')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]