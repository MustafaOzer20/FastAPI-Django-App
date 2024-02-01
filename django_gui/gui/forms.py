from django import forms

class DriverFilterForm(forms.Form):
    startDate = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), required=True)
    endDate = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), required=True)
    minScore = forms.FloatField(required=True)
    maxScore = forms.FloatField(required=True)
    limit = forms.IntegerField(min_value=1, max_value=150, required=True)
    offset = forms.IntegerField(min_value=0, required=True)