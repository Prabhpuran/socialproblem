# Generated by Django 5.1.2 on 2024-10-25 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_emergencyservice_location_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='case',
            name='category',
            field=models.CharField(choices=[('MR', 'Marital Rape'), ('DA', 'Domestic Abuse'), ('DW', 'Dowry Issues'), ('MA', 'Mental Harrasment')], max_length=2),
        ),
    ]
