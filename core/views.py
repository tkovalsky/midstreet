from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.template import loader, Context
from django.template.loader import get_template
from rest_framework import viewsets

#from .models import Contact
#from .forms import ContactForm

# Create your views here.
'''
def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            })
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['youremail@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('contact')

    return render(request, 'contact.html', {
        'form': form_class,
    })
'''


def home(request):
    #form = ContactForm(request.POST or None)
    #if form.is_valid():
    #    messages.success(request, 'Your message was sent') #this is optional but good for the user
    #context = {
    #    'form': form,   #here you are passing the variable "form" to the template so you can use it like "{{form.as_p}}"
    #    }
    #return render(request, 'home.html', context)
    return render(request, 'marketing.html')

def deals(request):
    return render(request, 'deals.html')
