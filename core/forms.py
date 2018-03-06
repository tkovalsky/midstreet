from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper

from .models import Deal
#from .models import Contact

class AddDealModelForm(forms.ModelForm):
    class Meta:

        model = Deal



'''
class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Your name:"
        self.fields['contact_email'].label = "Your email:"
        self.fields['content'].label = "What do you want to say?"
'''
