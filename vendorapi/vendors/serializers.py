from .models import Vendor
from rest_framework import serializers
from django.contrib.auth.models import User

# Create your serializers here.
class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'
        read_only_fields = ['user']  # Make user field read-only
        



class UserSignupSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['full_name', 'email']

    def create(self, validated_data):
        full_name = validated_data.pop('full_name') # Extract the full_name from the validated data

        user = User.objects.create(
            first_name=full_name,
            email=validated_data['email'],
            username=validated_data['email']  # Assuming username is the email
        )

        user.set_unusable_password()  # Set an unusable password
        user.save()  # Save the user instance
        return user