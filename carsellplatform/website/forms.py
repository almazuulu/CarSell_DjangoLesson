from django import forms

class ContactForm(forms.Form):
    full_name = forms.CharField(
        label = 'Full name',
        max_length=100,
        widget= forms.TextInput(attrs = {
            'class': 'form-control mb-3',
            'placeholder': 'Full Name',
        })
    )
    
    email = forms.EmailField(
        label = 'Email',
        widget= forms.EmailInput(attrs = {
            'class': 'form-control mb-3',
            'placeholder': 'Email',
        })
    )
    
    subject = forms.CharField(
        label = 'Subject',
        max_length=100,
        widget= forms.TextInput(attrs = {
            'class': 'form-control mb-3',
            'placeholder': 'Subject',
        })
    )
    
    phone = forms.CharField(
        label = 'Phone Number',
        max_length=100,
        widget= forms.TextInput(attrs = {
            'class': 'form-control mb-3',
            'placeholder': 'Phone Number',
        })
    )
    
    message = forms.CharField(
        label = 'Message',
        widget= forms.Textarea(attrs = {
            'class': 'form-control mb-3',
            'rows': 5,
            'placeholder': 'Enter your message',
        })
    )
    
    