# core/models.py
from django.db import models
from django.contrib.auth.models import User

class Case(models.Model):
    CATEGORY_CHOICES = [
        ('MR', 'Marital Rape'),
        ('DA', 'Domestic Abuse'),
        ('DW', 'Dowry Issues')
    ]
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    description = models.TextField()
    is_anonymous = models.BooleanField(default=False)
    status = models.CharField(max_length=20, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.get_category_display()} - {self.created_at}'

# core/models.py
class EmergencyService(models.Model):
    service_name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)
    service_type = models.CharField(max_length=100, choices=[('Shelter', 'Shelter'), ('Legal Aid', 'Legal Aid'), ('Medical', 'Medical'), ('Helpline', 'Helpline'), ('Police Aid','Police Aid')])
    location = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.service_name
