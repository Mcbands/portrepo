from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Name')
    email = forms.EmailField(label='Email')
    subject = forms.CharField(label='buject')
    message = forms.CharField(widget=forms.Textarea, label='Message')
