from django.shortcuts import render, redirect

from santkrupadoor.settings import EMAIL_HOST_USER
from .models import SliderImage, Slider, Header, Info, Footer, About, GalleryImage, Service, Blog, Testimonial, Contact
from .forms import ContactForm
# Create your views here.

# for sending email & contact
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.template import loader
from django.contrib import messages

def index(request):
    slider_images = SliderImage.objects.all()
    sliders = Slider.objects.all()
    header = Header.objects.first()
    info = Info.objects.first()
    footer = Footer.objects.first()
    about = About.objects.first()
    gallery_images = GalleryImage.objects.all()[:3]
    services = Service.objects.all()[:3]
    blogs = Blog.objects.all()[:2]
    testimonials = Testimonial.objects.all()
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            data = Contact()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.phone_number = form.cleaned_data['phone_number']
            data.message = form.cleaned_data['message']
            data.save()
            message = form.cleaned_data['message']
            name = form.cleaned_data['name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [EMAIL_HOST_USER,]
            html_message = loader.render_to_string(
                'email.html',
                {
                    'message':message,
                    'name':name,
                    'email':email,
                    'phone_number':phone_number,
                }
            )
            if message and email_from and recipient_list and html_message:
                try:
                    send_mail('New Contact Form Submission', '', email_from, recipient_list, html_message=html_message, fail_silently=False)
                except:
                    messages.error(request,"Cannot send mail right now, Try again later")
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                messages.success(request,"Message sent successfully")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                messages.error(request,"Please! Make sure all fields are entered and valid.")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request,"Please! Make sure all fields are entered and valid.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 
    return render(request, 'index.html', {'slider_images': slider_images , 'sliders': sliders, 'header': header, 'info': info, 'footer': footer, 'about': about, 'gallery_images': gallery_images, 'services': services, 'blogs': blogs, 'testimonials': testimonials, 'form': form})

def about(request):
    header = Header.objects.first()
    info = Info.objects.first()
    footer = Footer.objects.first()
    about = About.objects.first()
    return render(request, 'about.html', {'header': header, 'info': info, 'footer': footer, 'about': about})

def gallery(request):
    header = Header.objects.first()
    info = Info.objects.first()
    footer = Footer.objects.first()
    gallery_images = GalleryImage.objects.all()
    return render(request, 'gallery.html', {'header': header, 'info': info, 'footer': footer, 'gallery_images': gallery_images})

def service(request):
    header = Header.objects.first()
    info = Info.objects.first()
    footer = Footer.objects.first()
    services = Service.objects.all()
    return render(request, 'service.html', {'header': header, 'info': info, 'footer': footer, 'services': services})

def blog(request):
    header = Header.objects.first()
    info = Info.objects.first()
    footer = Footer.objects.first()
    blogs = Blog.objects.all()
    return render(request, 'blog.html', {'header': header, 'info': info, 'footer': footer, 'blogs': blogs})

def contact(request):
    header = Header.objects.first()
    info = Info.objects.first()
    footer = Footer.objects.first()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            data = Contact()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.phone_number = form.cleaned_data['phone_number']
            data.message = form.cleaned_data['message']
            data.save()
            message = form.cleaned_data['message']
            name = form.cleaned_data['name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [EMAIL_HOST_USER,]
            html_message = loader.render_to_string(
                'email.html',
                {
                    'message':message,
                    'name':name,
                    'email':email,
                    'phone_number':phone_number,
                }
            )
            if message and email_from and recipient_list and html_message:
                try:
                    send_mail('New Contact Form Submission', '', email_from, recipient_list, html_message=html_message, fail_silently=False)
                except:
                    messages.error(request,"Cannot send mail right now, Try again later")
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                messages.success(request,"Message sent successfully")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                messages.error(request,"Please! Make sure all fields are entered and valid.")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request,"Please! Make sure all fields are entered and valid.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 
        
    return render(request, 'contact.html', {'header': header, 'info': info, 'footer': footer})