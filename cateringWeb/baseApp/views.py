from django.shortcuts import render, get_object_or_404
from .models import MetaData,websiteDetail,HomeSection, AboutSection, WhyChooseSection, MenuCategory, MenuItem, EventsSection, ContactSection, BookADateSection
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import BookADateForm
from django.contrib import messages

# Create your views here.
def HomeView(request):
    # Fetch data from models
    absolute_url = request.build_absolute_uri()
    meta_data = MetaData.objects.first()
    web_details = websiteDetail.objects.first()
    home = HomeSection.objects.first()
    about = AboutSection.objects.first()
    why_choose = WhyChooseSection.objects.first()
    cat_menu = MenuCategory.objects.prefetch_related('menu_items')
    menu_items = MenuItem.objects.filter(is_available=True)
    events = EventsSection.objects.all()
    contact = ContactSection.objects.first()
    checkdate = BookADateSection.objects.first()

    message = None  # To store success or error message
    form = BookADateForm()

    if request.method == 'POST':
        form = BookADateForm(request.POST)
        if form.is_valid():
            # Save the booking request to the database
            booking = form.save()

            # Send an email notification to the admin
            admin_email = settings.ADMIN_EMAIL
            subject = f"New Catering Inquiry from {booking.customer_name}"
            email_message = (
                f"New inquiry details:\n\n"
                f"Name: {booking.customer_name}\n"
                f"Email: {booking.customer_email}\n"
                f"Phone: {booking.customer_phone}\n"
                f"Event Date: {booking.event_date}\n"
                f"Event Time: {booking.event_time}\n"
                f"Number of People: {booking.num_people}\n\n"
                f"Message:\n{booking.message}"
            )
            send_mail(
                subject,
                email_message,
                settings.DEFAULT_FROM_EMAIL,  # Sender's email
                [admin_email],  # Recipient's email
                fail_silently=False,
            )

            # Display success message
            messages.success(request, "Your inquiry has been submitted. We will contact you shortly.")

            form = BookADateForm()  # Clear the form after successful submission
            return redirect('/#book-a-table')

        else:
            # Display error message
            messages.error(request, "Error with your submission. Please retry or call us.")
            return redirect('/#book-a-table')
    else:
        form = BookADateForm()
    
    return render(request,'index.html', {
        'absolute_url' : absolute_url,
        'meta_data' : meta_data,
        'web_detail': web_details,
        'home': home,
        'about': about,
        'why_choose': why_choose,
        'menu_items': menu_items,
        'events': events,
        'contact': contact,
        'categorys': cat_menu,
        'checkdate': checkdate,
        'form': form,
        'message': message,
    })
"""
def CheckAdate(request):
    message = None  # To store success or error message

    if request.method == 'POST':
        form = BookADateForm(request.POST)
        if form.is_valid():
            # Save the booking request to the database
            booking = form.save()

            # Send an email notification to the admin
            admin_email = settings.ADMIN_EMAIL
            subject = f"New Catering Inquiry from {booking.customer_name}"
            email_message = (
                f"New inquiry details:\n\n"
                f"Name: {booking.customer_name}\n"
                f"Email: {booking.customer_email}\n"
                f"Phone: {booking.customer_phone}\n"
                f"Event Date: {booking.event_date}\n"
                f"Event Time: {booking.event_time}\n"
                f"Number of People: {booking.num_people}\n\n"
                f"Message:\n{booking.message}"
            )
            send_mail(
                subject,
                email_message,
                settings.DEFAULT_FROM_EMAIL,  # Sender's email
                [admin_email],  # Recipient's email
                fail_silently=False,
            )

            # Display success message
            message = {
                'type': 'success',
                'text': 'Your inquiry has been submitted. We will contact you shortly.',
            }

            form = BookADateForm()  # Clear the form after successful submission
        else:
            # Display error message
            message = {
                'type': 'error',
                'text': 'Error with your submission. Please retry or Call at the Phone Number below.',
            }
    else:
        form = BookADateForm()

    return render(request, 'index.html', {
        'form': form,
        'message': message,
    }) """