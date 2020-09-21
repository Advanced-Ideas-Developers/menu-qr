from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=50, 
        label=False, 
        required=True, 
        widget=forms.TextInput(attrs={'placeholder':'Nombre'}))
    from_email = forms.EmailField(
        required=True, 
        label=False, 
        widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    phone = forms.CharField(
        label=False, 
        required=False, 
        widget=forms.TextInput(attrs={'placeholder': 'Teléfono'}))
    message = forms.CharField(
        required=True, 
        label=False,
        widget=forms.Textarea(attrs={'placeholder':'Dejenos su mensaje'}))