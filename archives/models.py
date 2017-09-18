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
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return '%s' % self.catalogue_ref

    class Meta:
        ordering = ['catalogue_ref', ]


class TransationEvents(models.Model):
    source = models.ForeignKey(SourceMaterial)
    stock_number = models.IntegerField()
    purchase_date = models.DateField(null=True,
                                     blank=True)
    artist = models.ForeignKey('Person',
                               null=True,
                               blank=True,
                               related_name='Artist')
    reattributed = models.BooleanField()
    work = models.ForeignKey('Work')
    seller = models.ForeignKey('Person',
                               null=True,
                               blank=True,
                               related_name='Seller')
    encoded_cost = models.CharField(max_length=9, null=True,
                                    blank=True)
    purchase_pounds = models.IntegerField(null=True,
                                          blank=True)
    purchase_shillings = models.IntegerField(null=True,
                                             blank=True)
    purchase_pence = models.FloatField(null=True,
                                       blank=True)
    standardised_purchase_price = models.FloatField(null=True,
                                                    blank=True)
    target_pounds = models.IntegerField(null=True,
                                        blank=True)
    target_shillings = models.IntegerField(null=True,
                                           blank=True)
    target_pence = models.FloatField(null=True,
                                     blank=True)
    standardised_target_price = models.FloatField(null=True,
                                                  blank=True)
    buyer = models.ForeignKey('Person',
                              null=True,
                              blank=True,
                              related_name='Buyer')
    sold_date = models.DateField(null=True,
                                 blank=True)
    sold_pounds = models.IntegerField(null=True,
                                      blank=True)
    sold_shillings = models.IntegerField(null=True,
                                         blank=True)
    sold_pence = models.FloatField(null=True,
                                   blank=True)
    standardised_sold_price = models.FloatField(null=True,
                                                blank=True)
    owner = models.ForeignKey('Person',
                              null=True,
                              blank=True,
                              related_name='Owner')
    entry_line = models.IntegerField()
    entry_page = models.IntegerField()
    notes = models.TextField(null=True, blank=True)
    firm_owner = models.ForeignKey('Dealership',
                                   null=True,
                                   blank=True)

    def __str__(self):
        return '%s' % self.stock_number

    class Meta:
        verbose_name = 'Transaction event'
        verbose_name_plural = 'Transaction events'
        ordering = ('source', 'stock_number')


class Dealership(models.Model):
    description = models.CharField(max_length=50)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return '%s' % self.description


class Person(models.Model):
    first_name = models.CharField(max_length=30,
                                  null=True,
                                  blank=True)
    family_name = models.CharField(max_length=50)
    other_names = models.CharField(max_length=100,
                                   null=True, blank=True)
    title = models.ForeignKey('Title',
                              null=True, blank=True)
    location = models.ForeignKey('Location',
                                 blank=True, null=True)
    dob = models.IntegerField(null=True, blank=True)
    dod = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return '%s, %s' % (self.family_name, self.first_name)

    class Meta:
        ordering = ('family_name', 'first_name')


class Title(models.Model):
    description = models.CharField(max_length=50)

    def __str__(self):
        return '%s' % self.description


class Work(models.Model):
    title = models.TextField()
    genre = models.ForeignKey('Genre', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    artist = models.ForeignKey('Person', null=True,
                               blank=True)
    shape = models.ForeignKey('Shape', null=True,
                              blank=True)
    support = models.ForeignKey('Support', null=True,
                                blank=True)
    subject_location = models.ForeignKey('Location', null=True,
                                         blank=True)

    def __str__(self):
        if self.artist:
            artist = self.artist.family_name
        else:
            artist = 'Unidentified'
        return '%s, %s' % (self.title, artist)

    class Meta:
        ordering = ('artist__family_name', 'title')


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return '%s' % self.name


class Shape(models.Model):
    description = models.CharField(max_length=50)

    def __str__(self):
        return '%s' % self.description


class Support(models.Model):
    description = models.CharField(max_length=50)

    def __str__(self):
        return '%s' % self.description


class Location(models.Model):
    display_name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    point = models.GeometryField(blank=True,
                                 null=True,
                                 srid=4326)

    def __str__(self):
        return '%s' % self.display_name
