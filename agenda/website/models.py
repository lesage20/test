from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SiteInfo(models.Model):
    """ information about the website """
    
    name = models.CharField(max_length=30)
    icon = models.ImageField(upload_to='site-icons')
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    description = models.TextField()
    addresse = models.CharField(max_length=30)
    
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    class Meta():
        verbose_name = "Site Info"
        verbose_name_plural = "Site Infos"
        
    def __str__(self):
        return self.name

class Speaker(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'user')
    photo = models.ImageField(upload_to="users-icon")
    
    

    class Meta:
        verbose_name = ("Speaker")
        verbose_name_plural = ("Speakers")

    def __str__(self):
        return self.user.username






class Contact(models.Model):
    """these fields are about Contact sections """
    geolocation = models.URLField()
    message = models.TextField()
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    city_name = models.CharField( max_length=50)
    address = models.CharField(max_length=50)
    
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    class Meta():
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
    
    def __str__(self):
        return self.name 
    

    
class NewsLetter (models.Model):
    """ This is for the user to enter his email to receive news from us """
    
    email = models.EmailField()
    
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    class Meta():
        verbose_name = "Newsletter"
        verbose_name_plural = "Newsletters"
    
    def __str__(self):
        return self.email 

class SocialAccounts(models.Model):
    """ Site's social accounts """
    
    ICONS = [
        ("fa-facebok", "Facebook"),
        ("fa-twitter", "Twitter"),
        ("fa-pinterest", "Pinterest"),
        ("fa-linkedin", "LinkedIn"),
        ("fa-instagram", "Instagram"),
        
    ]
    
    name = models.CharField(max_length=30)
    link = models.URLField()
    icon = models.CharField(max_length=30, choices=ICONS)
    
    class Meta():
        verbose_name = "Social Account"
        verbose_name_plural = "Social Accounts"
    
    def __str__(self):
        return self.name 
    
class Entry(models.Model):
    
    title = models.CharField(max_length=50)
    
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Entry"
        verbose_name_plural = "Entries"

    def __str__(self):
        return self.title

class EntryContent(models.Model):
    
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE, related_name='entry')
    button = models.URLField(max_length=200)
    header = models.CharField(max_length=50)
    description = models.TextField()
    statistic = models.IntegerField()
    date = models.DateField()
    icon = models.ImageField(upload_to="entry-icons")
    
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    
    
    class Meta:
        verbose_name = "EntryContent"
        verbose_name_plural = "EntryContents"

    def __str__(self):
        return self.entry

