# Generated by Django 4.1 on 2023-09-05 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('city', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Structure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.CharField(blank=True, max_length=250, null=True)),
                ('name', models.CharField(max_length=100)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='city.city')),
            ],
        ),
    ]
