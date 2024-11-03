from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from django.utils.text import slugify
from django.utils.html import mark_safe
# from ckeditor.fields import RichTextField
import django.utils.timezone

def user_directory_path(instance,filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)
    
class Agence(models.Model):
    name    = models.CharField('Agence name', max_length=255, blank=True, null=False, default="Agence name")
    address = models.CharField(max_length=255, blank=True, null=True, default="Agence address")
    phone  = models.CharField('Contact Phone',max_length=255, blank=True, null=True, default="Agence phone")
    email  = models.EmailField('Email Address', max_length=255, default="agencemail@gmail.com")
    logo = models.ImageField(upload_to='agence', default='logo.jpg', blank=True, verbose_name=_('logo'))
    image = models.ImageField(blank=True, default='agence image', upload_to="agence")
    about_us = models.TextField(null=True, blank=True, default="About Us")


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural= 'Agences'

    # @property
    def logoURL(self):
        try:
            url = self.logo.url
        except:
            url = ''
        return url
    
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
    def agencelogo(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.logo.url))
    
class Brand(models.Model):
    name  = models.CharField('Brand name', max_length=255, default="Brand name")
    image = models.ImageField(upload_to='brand-images', default='brand.jpg', blank=True, verbose_name=_('Brand'))
    start = models.DateField(verbose_name=_('Start at'))
    end   = models.DateField(verbose_name=_('End at'))
    is_active = models.BooleanField(default=False)
   
    def __str__(self):
        return  f"{self.name}" 
    
    class Meta:
        ordering = ['-start'] #, '-created']
      
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
    def brand_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

class Type(models.Model):
    name   = models.CharField(max_length=100, verbose_name=_("Type")) #,default='name of the category', help_text='name of catygory')
    slug   = models.SlugField(blank=True,null=True)
    image  = models.ImageField(upload_to='type-images', default='type.jpg')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural= 'types'
      
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Type, self).save(*args, **kwargs)            
      
    def get_absolute_url(self):
        return reverse('index')
        # return 'https://www.google.fr'
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
    def type_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

STATUS = (
        ('For Sale' , 'For Sale'),
        ('For Rent' , 'For Rent'),
        ('Sold Out' , 'Sold Out'),

)
class Property(models.Model):
    status = models.CharField(choices=STATUS, default='', max_length=30, help_text='For Sale, For Rent,', )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='type')
    title = models.CharField(max_length=128, verbose_name =_('title of property'))
    slug = models.SlugField(blank=True,null=True)
    address = models.CharField(max_length=255, blank=True, null=True, default="Property adress")

    description = models.TextField(null=True,blank=True, default='This property is ...', help_text='infos about ', verbose_name =_('informations about product')) #description = RichTextField(blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    old_price = models.DecimalField(max_digits=12, decimal_places=2, default=0, blank=True,null=True, verbose_name =_('old price'))
    image   = models.ImageField(upload_to='property', default='property.jpg') # upload_to=user_directory_path it's for users
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Updated at'))
    is_active = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    is_slider = models.BooleanField(default=False) 
    # features = models.CharField(max_length=128, verbose_name =_('features of property'))
    rooms = models.IntegerField(verbose_name=_('rooms'))
    beds = models.IntegerField(verbose_name=_('beds'))
    baths = models.IntegerField(verbose_name=_('baths'))
    squart = models.IntegerField(verbose_name=_('squart'))

    def __str__(self):
        return  f"{self.title}" # ({self.description[0:50]})"
    
    class Meta:
        ordering = ['-updated', '-created']
        verbose_name = _("Property")
        verbose_name_plural = _("Properties")
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Property, self).save(*args, **kwargs)
            
    def get_absolute_url(self):
        return reverse("property-detail", kwargs={"slug":self.slug})
        # return reverse('index')
        # return 'https://www.google.fr'
    
    # @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
    def property_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    # def get_precentage(self):
    #     new_price = (self.price / self.old_price) * 100
    #     return new_price
    
class PropertyImages(models.Model):
    property    = models.ForeignKey(Property, on_delete=models.SET_NULL, null=True, related_name='images', verbose_name=_("Property"))
    image       = models.ImageField(upload_to='property-images', default='property.jpg') #/%y/%m/%d')
    description = models.CharField(max_length=64, blank=True, null=True, verbose_name=_("Description"))
    date        = models.DateTimeField(auto_now_add=True )
    # expirationTime = models.DateTimeField('expiration time (of ad)', default=timezone.now() + datetime.timedelta(days=30))

    class Meta:
        verbose_name_plural = _("Property Images") 
        
    def __str__(self):
        return self.image.name
      
    # @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Client(models.Model):
    name = models.CharField(max_length=40, blank=True, null=True, verbose_name=_("name"))
    profession = models.CharField(max_length=60, blank=True, null=True, verbose_name=_("profession"))
    image = models.ImageField(upload_to='client', default='client.jpg') #/%y/%m/%d')
    comment = models.TextField(blank=True, null=True, verbose_name =_("content"))
    slug = models.SlugField(blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('updated at'))
    is_shown = models.BooleanField(default=False)
    
    def __str__(self):
        return  f"{self.name}" # ({self.description[0:50]})"
    
    class Meta:
        ordering = ['-updated', '-created']
        
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
    def client_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    
class Service(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, verbose_name=_("service"))
    comment = models.TextField(blank=True, null=True, verbose_name =_("content"))
    image   = models.ImageField(upload_to='service', default='service.jpg') 
    created = models.DateTimeField(auto_now_add=True, verbose_name =_('created at'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('updated at'))
    is_shown = models.BooleanField(default=False)
    
    def __str__(self):
        return  f"{self.name}" # ({self.description[0:50]})"
    
    class Meta:
        ordering = ['-updated', '-created']
        
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
    def service_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
   
class Agent(models.Model):
    name = models.CharField(max_length=40, blank=True, null=True, verbose_name=_("name"))
    profession = models.CharField(max_length=60, blank=True, null=True, verbose_name=_("profession"))
    image = models.ImageField(upload_to='agent', default='agent.jpg') #/%y/%m/%d')
    email = models.EmailField(max_length=255,blank=True, null=True,  default="", help_text='agentmail@gmail.com', verbose_name=_("Email address"))
    mobile  = models.CharField(max_length=20, verbose_name = _("mobile")) 
    slug = models.SlugField(blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('updated at'))
    
    def __str__(self) -> str:
        return self.name 
    
    class Meta:
        ordering = ['-updated', '-created']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Agent, self).save(*args, **kwargs)
            
    def get_absolute_url(self):
        return reverse("agent-detail", kwargs={"slug":self.slug})
            
    # @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
    def agent_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

class Blog(models.Model):  
    author = models.CharField(max_length=64, blank=True, null=True, verbose_name=_("author"))
    subject = models.CharField(max_length=64, blank=True, null=True, verbose_name=_("subject"))
    comment = models.TextField(blank=True, null=True, verbose_name =_("content"))
    image   = models.ImageField(upload_to='blog', default='blog.jpg') 
    created = models.DateTimeField(auto_now_add=True, verbose_name =_('Created at'))
    updated = models.DateTimeField(auto_now=True, verbose_name =_('Updated at'))
    
    is_shown = models.BooleanField(default=False)
    
    def __str__(self):
        return  f"{self.author}" # ({self.description[0:50]})"
    
    class Meta:
        ordering = ['-updated', '-created']
        
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
    def blog_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    
class Message(models.Model):  
    author = models.CharField(max_length=64, blank=True, null=True, verbose_name=_("author"))
    email = models.EmailField()
    subject = models.CharField(max_length=64, blank=True, null=True, verbose_name=_("subject"))
    comment = models.TextField(blank=True, null=True, verbose_name=_("content"))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Updated at'))
    
    def __str__(self):
        return  f"{self.author}" # ({self.description[0:50]})"
    
    class Meta:
        ordering = ['-updated', '-created']