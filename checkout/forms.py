from django import forms
from .models import Order
from django.forms import Select
 
 
class MakePaymentForm(forms.Form):
    
    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2018, 2036)]
   
    credit_card_number = forms.CharField(label ='Credit card number', required=False)
    cvv = forms.CharField(label='Security code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label="Month", choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label="Year", choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput, required=False)
 
class OrderCreateForm(forms.ModelForm):
    

    class Meta:
        COUNTRY_CHOICES = (('Australia', 'Australia'), ('Austria', 'Austria'), ('Belgium', 'Belgium'), ('Canada', 'Canada'), 
        ('Denmark', 'Denmark'), ('Finland', 'Finland'), ('France', 'France'),
        ('Germany', 'Germany'), ('Hong Kong', 'Hong Kong'), ('Ireland', 'Ireland'), ('Japan', 'Japan'), 
        ('Luxembourg', 'Luxembourg'), ('Netherlands', 'Netherlands'), ('New Zealand', 'New Zealand'), ('Norway', 'Norway'),
        ('Singapore', 'Singapore'), ('Spain', 'Spain'), ('Sweden', 'Sweden'), ('Switzerland', 'Switzerland'), 
        ('United Kingdom', 'United Kingdom'), ('United States', 'United States'),('Italy', 'Italy'),('Portugal', 'Portugal'),
        ('Poland', 'Poland')
        )
        
        model = Order
        

        widgets = {'country': Select( choices=COUNTRY_CHOICES), 'user': forms.HiddenInput() }
        fields = ('user', 'full_name', 'phone_number', 'country', 'postcode', 'town_or_city', 'street_address1',
        'street_address2', 'county')
