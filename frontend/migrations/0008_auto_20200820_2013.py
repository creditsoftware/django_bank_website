# Generated by Django 2.1.5 on 2020-08-20 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0007_auto_20200820_1959'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='incomeproof',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='incometype',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='loan',
            name='currency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='frontend.Currency'),
        ),
        migrations.AlterField(
            model_name='loansecurity',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='purpose',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='workindustry',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
