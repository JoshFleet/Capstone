from django import forms
from .models import GroupListing

class GroupCreateView(forms.ModelForm):
    terms_And_Conditions = forms.BooleanField(required=True)

    class Meta:
        model = GroupListing
        fields = ['group_Name', 'image', 'date', 'location', 'description', 'terms_And_Conditions']

class GroupUpdateForm(forms.ModelForm):
    class Meta:
        model = GroupListing
        fields = ['group_Name', 'image', 'date', 'location', 'description', 'terms_And_Conditions']
