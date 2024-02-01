from django import forms

class DriverFilterForm(forms.Form):
    startDate = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), required=False)
    endDate = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), required=False)
    minScore = forms.FloatField(required=False)
    maxScore = forms.FloatField(required=False)
    limit = forms.IntegerField(min_value=1, required=False)
    offset = forms.IntegerField(min_value=0, required=False)