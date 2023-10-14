from django.db import models

# Create your models here.
class SliderImage(models.Model):
    image = models.ImageField(upload_to='images/')
    
class NavigationLink(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    header = models.ForeignKey('Header', related_name='navigation_links', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class Header(models.Model):
    website_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.website_name
    
class Slider(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    button_link = models.CharField(max_length=255)
    
class Info(models.Model):
    company_name = models.CharField(max_length=255)
    company_description = models.TextField()
    company_description_1 = models.TextField(default=1) # type: ignore
    location = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    facebook_link = models.URLField(blank=True)
    google_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)
    instagram_link = models.URLField(blank=True)

    def __str__(self):
        return self.company_name
    
class Footer(models.Model):
    description = models.CharField(max_length=255)
    description_1 = models.URLField(blank=True, default=1) # type: ignore

    def __str__(self):
        return self.description
    
class About(models.Model):
    heading = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', default=1)
    description = models.TextField()

    def __str__(self):
        return self.heading
    
class GalleryImage(models.Model):
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.image.name
    
class Service(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()

    def __str__(self):
        return self.title
    
class Blog(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blogs/')
    description = models.TextField()

    def __str__(self):
        return self.title
    
class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='testimonials')
    content = models.TextField()
    
    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name