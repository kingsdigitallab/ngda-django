from django.contrib.gis import admin


from archives.models import SourceMaterial, TransationEvents,\
    Person, Title, Work, Support, Shape, Location, Genre,\
    Dealership


class LocationAdmin(admin.OSMGeoAdmin):
    openlayers_url = 'https://openlayers.org/api/2.13.1/OpenLayers.js'


class SourceMaterialAdmin(admin.OSMGeoAdmin):
    list_display = ('__str__', 'title')


class TransactionAdmin(admin.OSMGeoAdmin):
    list_display = ('__str__', 'source')


class PersonAdmin(admin.OSMGeoAdmin):
    list_display = ('__str__', 'dob', 'dod')

# Register your models here.


admin.site.register(SourceMaterial, SourceMaterialAdmin)
admin.site.register(TransationEvents, TransactionAdmin)
admin.site.register(Genre)
admin.site.register(Person)
admin.site.register(Title)
admin.site.register(Work)
admin.site.register(Support)
admin.site.register(Shape)
admin.site.register(Location, LocationAdmin)
admin.site.register(Dealership)
