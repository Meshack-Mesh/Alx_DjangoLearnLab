# blog/forms.py
from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required. Enter a valid email address.")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("bio", "avatar")
        widgets = {
            "bio": forms.Textarea(attrs={"rows":3}),
        }

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "email")
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter a title', 'class': 'form-control'}),
            'content': forms.Textarea(attrs={'placeholder': 'Write the content here...', 'rows': 10, 'class': 'form-control'}),
        }
