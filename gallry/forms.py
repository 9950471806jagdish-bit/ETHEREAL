from django import forms
# pyrefly: ignore [missing-import]
from .models import Profile

class ProfilePhotoForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']