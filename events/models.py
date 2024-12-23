from django.db import models

class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=120)
    address = models.CharField(max_length=300)
    zip_code = models.CharField('Zip Code',max_length=15)
    phone = models.CharField('contact_phone',max_length=25)
    web = models.URLField('Website Address')
    email = models.EmailField('Email Address')

    def __str__(self):
        return self.name


class MyClubUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name =models.CharField(max_length=30)
    email = models.EmailField('User Email')

    def __str__(self):
        return self.first_name #+ ' ' + self.last_name
class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateTimeField('Event Date')
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, blank=True, null=True)
    #venue = models.CharField(max_length=120)
    manager = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(MyClubUser , blank=True)



    def __str__(self):
        return self.name