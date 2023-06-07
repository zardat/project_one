from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django import forms
from django.contrib.auth.password_validation import validate_password


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
      token = super().get_token(user)
      # Add custom claims
      token['username'] = user.username
      token['email'] = user.email
      # ...
      return token
   
class RegisterSerializer(serializers.ModelSerializer):
   # phone_no = forms.CharField(max_length = 20)
   # password1 = serializers.CharField(write_only=True, required=True, validators=[validate_password])
   # password2 = serializers.CharField(write_only=True, required=True)
   # email = forms.EmailField()
   # phone_no = forms.CharField(max_length = 20)
   # first_name = forms.CharField(max_length = 20)
   # last_name = forms.CharField(max_length = 20)
   class Meta:
      model = User
      fields = ['username', 'email'] 