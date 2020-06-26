from django.db import models
from website.models import Speaker
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='category')
    description= models.TextField()
    
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    class Meta():
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.nom



class UpcomingEvent(models.Model):
    icon = models.ImageField(upload_to="upcomingevent-icons")
    begin_date = models.DateTimeField()
    end_date = models.DateTimeField()
    title = models.CharField(max_length=50)
    speakers = models.ForeignKey(Speaker, on_delete=models.CASCADE, related_name='speakers')
    
    date_add = models.DateField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    
    class Meta:
        verbose_name = ("UpcomingEvent")
        verbose_name_plural = ("UpcomingEvents")

    def __str__(self):
        return self.title



class Event(models.Model):
    image = models.ImageField(upload_to='Events')
    title = models.CharField(max_length=50)
    location = models.URLField()
    begin_date = models.DateTimeField()
    end_date = models.DateTimeField()
    buy = models.URLField(max_length=200)
    venue = models.TextField()
    organizer = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='tag')
    basic_ticket_price = models.IntegerField()
    vip_ticket_price = models.IntegerField()
    number_of_ticket = models.IntegerField()
    
    
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    

    class Meta:
        verbose_name = ("single-event")
        verbose_name_plural = ("single-events")

    def __str__(self):
        return self.name

# class Search(models.Model):
#     date = models.DateField()
#     events = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="events")
#     location = models.CharField(max_length=50)
#     button = models.URLField(max_length=50)
    

#     class Meta:
#         verbose_name = ("Search")
#         verbose_name_plural = ("Searchs")

#     def __str__(self):
#         return self.event
    
