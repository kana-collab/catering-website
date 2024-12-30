from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile



class MetaData(models.Model):
    description = models.TextField(verbose_name="Meta Description")
    keywords = models.TextField(verbose_name="Meta Keywords")
    author = models.CharField(verbose_name="Author/Business Name", max_length=100)

    def __str__(self):
        return self.description


class websiteDetail(models.Model):
    headline = models.CharField(max_length=200, verbose_name="Headline")
    title_logo = models.ImageField(upload_to='favicon/', verbose_name="title icon",)  
    #logo = models.ImageField(upload_to='logo/', verbose_name="Business logo", null=True)
    #logo_description = models.CharField(max_length=400, verbose_name='logo description', blank=True)

    def __str__(self):
        return self.headline


class HomeSection(models.Model):
    headline = models.CharField(max_length=200, verbose_name="Headline")
    title_text = models.CharField(max_length=100, verbose_name="Title Text")
    description = models.TextField(verbose_name="Description")
    cta_button_text = models.CharField(max_length=100, verbose_name="CTA Button Text")
    watch_video_button_link = models.URLField(verbose_name="Watch Video Button Link")
    dish_image = models.ImageField(upload_to='home/', verbose_name="Dish Image")
    image_description = models.CharField(max_length=400, verbose_name='dish image description', blank=True)

    def __str__(self):
        return self.headline


class AboutSection(models.Model):
    description = models.CharField(max_length=100, verbose_name="About Description")
    paragraph1 = models.TextField(verbose_name="Paragraph 1")
    bullet1 = models.TextField(verbose_name="Bullet Point 1")
    bullet2 = models.TextField(verbose_name="Bullet Point 2")
    bullet3 = models.TextField(verbose_name="Bullet Point 3")
    paragraph2 = models.TextField(verbose_name="Paragraph 2")
    phone_number = models.CharField(max_length=15, verbose_name="Phone Number")
    about_image1 = models.ImageField(upload_to='about/', verbose_name="About Image 1", default='default.jpg1')
    image1_description = models.CharField(max_length=400, verbose_name='Image 1 description', default='default')
    about_image2 = models.ImageField(upload_to='about/', verbose_name="About Image 2", default='default.jpg2')
    image2_description = models.CharField(max_length=400, verbose_name='Image 1 description', default='default')
 
    def __str__(self):
        return self.description


class WhyChooseSection(models.Model):
    paragraph1 = models.TextField(verbose_name="Paragraph 1")
    card1_title = models.CharField(max_length=100, verbose_name="Card 1 Title")
    card1_paragraph = models.TextField(verbose_name="Card 1 Paragraph")
    card2_title = models.CharField(max_length=100, verbose_name="Card 2 Title")
    card2_paragraph = models.TextField(verbose_name="Card 2 Paragraph")
    card3_title = models.CharField(max_length=100, verbose_name="Card 3 Title")
    card3_paragraph = models.TextField(verbose_name="Card 3 Paragraph")

    def __str__(self):
        return self.paragraph1[:50]  # Display first 50 characters of the paragraph


class MenuCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Category Name")
    description = models.TextField(blank=True, null=True, verbose_name="Description")

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=100, verbose_name="Dish Name")
    description = models.TextField(verbose_name="Description")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Price")
    category = models.ForeignKey(
        MenuCategory,
        on_delete=models.CASCADE,
        related_name='menu_items',
        verbose_name="Category"
    )
    is_available = models.BooleanField(default=True, verbose_name="Is Available")
    image = models.ImageField(upload_to='menu/', verbose_name="Image")
    image_description = models.CharField(max_length=400, verbose_name='item image description', blank=True)


    def save(self, *args, **kwargs):
        # Save the uploaded image first
        super().save(*args, **kwargs)

        if self.image:
            # Open the saved image
            img = Image.open(self.image)

            # Define the maximum width and height for the image
            max_width = 500
            max_height = 500

            # Get original image dimensions
            width, height = img.size

            # Calculate the ratio to preserve aspect ratio
            aspect_ratio = width / height

            # Resize based on the aspect ratio
            if width > height:
                new_width = max_width
                new_height = int(max_width / aspect_ratio)
            else:
                new_height = max_height
                new_width = int(max_height * aspect_ratio)

            # Resize the image while preserving the aspect ratio
            img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

            # Create a new image with a white background (padding)
            new_img = Image.new("RGB", (max_width, max_height), (255, 255, 255))  # White background

            # Calculate position to paste the resized image on the white background
            paste_x = (max_width - new_width) // 2
            paste_y = (max_height - new_height) // 2

            # Paste the resized image onto the white background
            new_img.paste(img, (paste_x, paste_y))

            # Save the resized and cropped image back to the same field
            buffer = BytesIO()
            new_img.save(buffer, format='JPEG')  # You can change the format if needed
            resized_image_file = ContentFile(buffer.getvalue())
            self.image.save(self.image.name, resized_image_file, save=False)  # Overwrite the same field

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class EventsSection(models.Model): 
    name = models.CharField(max_length=100, verbose_name="Event Name")
    picture = models.ImageField(upload_to="events/", verbose_name="Event Picture")
    image_description = models.CharField(max_length=200, verbose_name="Event Image description", default='default')
    description = models.TextField(verbose_name="Event Description", max_length=200)

    def __str__(self):
        return self.name


class BookADateSection(models.Model):
    image = models.ImageField(upload_to="book_a_date/", verbose_name="Card Image")
    image_description = models.CharField(max_length=400, verbose_name='BookADate Section Image Description', default='default')

    def __str__(self):
        return f"Book a Date Image {self.pk}"


class BookADateForm(models.Model):
    customer_name = models.CharField(max_length=100, verbose_name="Customer Name")
    customer_email = models.EmailField(max_length=100, verbose_name="Customer Email")
    customer_phone = models.CharField(max_length=15, verbose_name="Customer Phone Number")
    event_date = models.DateField(verbose_name="Date of Event")
    event_time = models.TimeField(verbose_name="Time of Event")
    num_people = models.PositiveIntegerField(verbose_name="Number of People")
    message = models.TextField(verbose_name="Message")

    def __str__(self):
        return self.customer_name


class ContactSection(models.Model):
    opening_hours = models.TextField(verbose_name="Calling Hours")
    phone_number = models.CharField(max_length=20, verbose_name="Phone Number")
    email = models.EmailField(verbose_name="Email Address")

    def __str__(self):
        return f"Contact Info for {self.phone_number}"
