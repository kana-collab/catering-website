# forms.py
from django import forms
from django.forms import TextInput, EmailInput, NumberInput, DateInput, TimeInput, Textarea
from .models import BookADateForm
from datetime import date

class BookADateForm(forms.ModelForm):
    class Meta:
        model = BookADateForm
        fields = ['customer_name', 'customer_email', 'customer_phone', 'event_date', 'event_time', 'num_people', 'message']
        widgets = {
            'customer_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'customer_email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'customer_phone': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
            'event_date': DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'event_time': TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'num_people': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of people'}),
            'message': Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Add additional details'}),
        }
    
    def clean_event_date(self):
        event_date = self.cleaned_data['event_date']
        if event_date < date.today():
            raise forms.ValidationError("The event date cannot be in the past.")
        return event_date

    def clean_customer_phone(self):
        customer_phone = self.cleaned_data['customer_phone']
        if not customer_phone.isdigit():
            raise forms.ValidationError("Phone number must contain only digits.")
        return customer_phone
    
    
