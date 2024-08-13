from rest_framework import serializers

from flirtify.models import UserData

from django.core.validators import EmailValidator, RegexValidator

class Serializationclass(serializers.ModelSerializer):
    name = serializers.CharField(
        validators=[RegexValidator(
            regex='^[a-zA-Z\s]+$',
            message='Name must contain only letters and spaces.',
            code='invalid_name'
        )]
    )
    email = serializers.EmailField(
        validators=[EmailValidator(message="Enter a valid email address.")]
    )
    dob = serializers.DateField(
        error_messages={'invalid': 'Enter a valid date.'}
    )
    address = serializers.CharField(
        validators=[RegexValidator(
            regex='^[a-zA-Z\s]+$',
            message='address must contain only letters and spaces.',
            code='invalid_address'
        )]
    )
    phone_number = serializers.CharField(
        validators=[RegexValidator(
            regex='^\+?1?\d{9,15}$',  # Adjust regex as per your requirement
            message='Phone number must be entered in the format: "+999999999". Up to 15 digits allowed.',
            code='invalid_phone_number'
        )]
    )
    class Meta:
        model = UserData
        fields = '__all__'

class UserDataSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        validators=[RegexValidator(
            regex='^[a-zA-Z\s]+$',
            message='Name must contain only letters and spaces.',
            code='invalid_name'
        )]
    )
    email = serializers.EmailField(
        validators=[EmailValidator(message="Enter a valid email address.")]
    )
    dob = serializers.DateField(
        error_messages={'invalid': 'Enter a valid date.'}
    )
    address = serializers.CharField(
        validators=[RegexValidator(
            regex='^[a-zA-Z\s]+$',
            message='address must contain only letters and spaces.',
            code='invalid_address'
        )]
    )
    phone_number = serializers.CharField(
        validators=[RegexValidator(
            regex='^\+?1?\d{9,15}$',  # Adjust regex as per your requirement
            message='Phone number must be entered in the format: "+999999999". Up to 15 digits allowed.',
            code='invalid_phone_number'
        )]
    )
    
    def validate_email(self, value):
        # Check if email already exists
        if UserData.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already registered.")
        return value

    class Meta:
        model = UserData
        fields = ['name', 'email', 'phone_number', 'dob', 'address']

class UpdateDataSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        validators=[RegexValidator(
            regex='^[a-zA-Z\s]+$',
            message='Name must contain only letters and spaces.',
            code='invalid_name'
        )]
    )
    email = serializers.EmailField(
        validators=[EmailValidator(message="Enter a valid email address.")]
    )
    dob = serializers.DateField(
        error_messages={'invalid': 'Enter a valid date.'}
    )
    address = serializers.CharField(
        validators=[RegexValidator(
            regex='^[a-zA-Z\s]+$',
            message='address must contain only letters and spaces.',
            code='invalid_address'
        )]
    )
    phone_number = serializers.CharField(
        validators=[RegexValidator(
            regex='^\+?1?\d{9,15}$',  # Adjust regex as per your requirement
            message='Phone number must be entered in the format: "+999999999". Up to 15 digits allowed.',
            code='invalid_phone_number'
        )]
    )

    class Meta:
        model = UserData
        fields = ['name', 'email', 'phone_number', 'dob', 'address']