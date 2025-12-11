from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name", "bio", "profile_picture"]


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "first_name", "last_name", "bio"]

    def create(self, validated_data):
        # Use the built-in create_user method (handles password hashing)
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(required=False, allow_blank=True)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")

        if not (username or email):
            raise serializers.ValidationError("Provide username or email to login.")

        if email and not username:
            try:
                user_obj = User.objects.get(email__iexact=email)
                username = user_obj.username
            except User.DoesNotExist:
                raise serializers.ValidationError("Invalid credentials")

        user = authenticate(username=username, password=password)

        if not user:
            raise serializers.ValidationError("Invalid credentials")

        data["user"] = user
        return data
