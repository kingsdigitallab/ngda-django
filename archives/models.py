from django.contrib.gis.db import models

# Create your models here.


class SourceMaterial(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    page_count = models.IntegerField()
    lines_per_page = models.IntegerField()
    line_height = models.FloatField()
    catalogue_ref = models.CharField(max_length=30)


class TransationEvents(models.Model):
    source = models.ForeignKey(SourceMaterial)
    stock_number = models.IntegerField()
    purchase_date = models.DateField()
    artist = models.ForeignKey('Person',
                               null=True,
                               related_name='Artist')
    reattributed = models.BooleanField()
    work = models.ForeignKey('Work')
    seller = models.ForeignKey('Person',
                               null=True,
                               related_name='Seller')
    purchase_pounds = models.IntegerField()
    purchase_shillings = models.IntegerField()
    purchase_pence = models.FloatField()
    standardised_purchase_price = models.FloatField()
    target_pounds = models.IntegerField()
    target_shillings = models.IntegerField()
    target_pence = models.FloatField()
    standardised_target_price = models.FloatField()
    buyer = models.ForeignKey('Person',
                              null=True,
                              related_name='Buyer')
    sold_pounds = models.IntegerField()
    sold_shillings = models.IntegerField()
    sold_pence = models.FloatField()
    standardised_sold_price = models.FloatField()
    owner = models.ForeignKey('Person',
                              null=True,
                              related_name='Owner')
    entry_line = models.IntegerField()
    entry_page = models.IntegerField()


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    family_name = models.CharField(max_length=50)
    other_names = models.CharField(max_length=100)
    title = models.ForeignKey('Title', null=True)
    location = models.ForeignKey('Location')


class Title(models.Model):
    description = models.CharField(max_length=50)


class Work(models.Model):
    description = models.TextField(null=True)
    artist = models.ForeignKey('Person')
    shape = models.ForeignKey('Shape')
    support = models.ForeignKey('Support')
    subject_location = models.ForeignKey('Location')


class Shape(models.Model):
    description = models.CharField(max_length=50)


class Support(models.Model):
    description = models.CharField(max_length=50)


class Location(models.Model):
    display_name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    point = models.GeometryField(blank=True,
                                 null=True,
                                 srid=4326)
