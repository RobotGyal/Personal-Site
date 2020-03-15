from django import forms

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    contact_subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)