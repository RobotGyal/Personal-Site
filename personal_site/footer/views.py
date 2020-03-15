from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.template.loader import get_template

from django.http import HttpResponse, HttpResponseRedirect


def about(request):
    return render(request, 'footer/about.html')


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
            contact_subject = request.POST.get(
                'contact_subject'
            , '')
            message = request.POST.get(
                'message'
            , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('footer/contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'contact_subject': contact_subject,
                'message': message
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['aleiaknight@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('success')

    return render(request, 'footer/contact.html', {
        'form': form_class,
    })

def success(request):
    content={
        messaage:"Success! Thank you for your message."
    }
    return redirect()