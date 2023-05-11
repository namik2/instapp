from django import forms
from stats.models import IntagramStats



class InstagramAddForm(forms.ModelForm):

    class Meta:
        model = IntagramStats
        fields = (
            'username',
            'password'
        )