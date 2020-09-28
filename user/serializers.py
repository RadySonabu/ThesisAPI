from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import MyUser


class UserInputSerializer(serializers.ModelSerializer):
    """ Serializer for User Create and Update """
    
    class Meta:
        model = MyUser
        fields = [
            'email', 'password',
            'role',
            'first_name', 'middle_name', 'last_name', 'age', 'blood_type',
            'phone_number',
            'street', 'city', 'barangay', 'postal_code',
             ]

    def create(self, validated_data):
        user = MyUser.objects.create_user(
            username=validated_data['email'], 
            email= validated_data['email'], 
            password=validated_data['password'], 
            first_name=validated_data['first_name'], 
            middle_name=validated_data.get('middle_name', None), 
            last_name=validated_data['last_name'],
            age=validated_data['age'], 
            blood_type=validated_data['blood_type'], 
            street=validated_data['street'], 
            barangay=validated_data['barangay'], 
            city=validated_data['city'], 
            postal_code=validated_data['postal_code'], 
            phone_number=validated_data['phone_number'], 
            role=validated_data.get('role', False), 
            active_status=True, 
            )

        return user


class UserOutputSerializer(serializers.ModelSerializer):
    """ Serializer for User Retrieve """

    class Meta:
        model = MyUser
        fields = [
            'id',
            'email', 'password',
            'role',
            'first_name', 'middle_name', 'last_name', 'age', 'blood_type',
            'phone_number',
            'street', 'city', 'barangay', 'postal_code',
            'date_created', 'date_updated', 'active_status'
             ]


class UserLoginSerializer(serializers.Serializer):
    """ Serializer for User login """

    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")

    