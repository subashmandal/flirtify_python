from django.db import models
from django.core.validators import RegexValidator, EmailValidator
from django.utils import timezone

class UserData(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[RegexValidator(
            regex='^[a-zA-Z\s]+$',
            message='Name must contain only letters and spaces.',
            code='invalid_name'
        )]
    )
    email = models.EmailField(
        validators=[EmailValidator(message="Enter a valid email address.")]
    )
    dob = models.DateField(
        validators=[],
        error_messages={
            'invalid': 'Enter a valid date.'
        }
    )
    address = models.CharField(max_length=255, null=True, blank= True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    
    class Meta:
        db_table = 'user_data'
    