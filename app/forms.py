from django import forms
from app.models import *

class ContactForm(forms.ModelForm):
    # name = forms.CharField(required=True, max_length=255)
    # phone_number = forms.CharField(required=True, max_length=255)
    # email = forms.EmailField(required=True)
    # message = forms.TimeField(required=True)
    
    class Meta:
        model = Contact
        fields = ['name', 'phone_number', 'email', 'message']
        
        
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Your Name'
        self.fields['name'].widget.attrs['type'] = 'text'
        self.fields['email'].widget.attrs['type'] = 'email'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Phone Number'
        self.fields['phone_number'].widget.attrs['type'] = 'text'
        self.fields['message'].widget.attrs['placeholder'] = 'Message'
        self.fields['message'].widget.attrs['class'] = 'message-box'
        
        
class AdminContactForm(forms.ModelForm):
    # name = forms.CharField(required=True, max_length=255)
    # phone_number = forms.CharField(required=True, max_length=255)
    # email = forms.EmailField(required=True)
    # message = forms.TimeField(required=True)
    
    class Meta:
        model = Contact
        fields = ['name', 'phone_number', 'email', 'message']
        
    def __init__(self, *args, **kwargs):
        super(AdminContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Your Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['phone'].widget.attrs['placeholder'] = 'Phone Number'
        self.fields['message'].widget.attrs['placeholder'] = 'Message'
        self.fields['name'].widget.attrs['type'] = 'text'
        self.fields['phone'].widget.attrs['type'] = 'text'
        self.fields['email'].widget.attrs['type'] = 'email'