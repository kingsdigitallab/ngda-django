from django.contrib.gis import admin


from archives.models import SourceMaterial, TransationEvents,\
    Person, Title, Work, Support, Shape, Location, Genre,\
    Dealership, PageImage, WorkImage, Commission, Nationality,\
    SubGenre, School, Movement, CurrentLocation, LocationType


class LocationAdmin(admin.OSMGeoAdmin):
    openlayers_url = 'https://openlayers.org/api/2.13.1/OpenLayers.js'


class SourceMaterialAdmin(admin.OSMGeoAdmin):
    list_display = ('__str__', 'title')

class WorkImageInline(admin.StackedInline):
    model = WorkImage

class WorkAdmin(admin.OSMGeoAdmin):
    inlines = (WorkImageInline,)    

class TransactionAdmin(admin.OSMGeoAdmin):
    list_display = ('__str__', 'source', 'work')

class PersonAdmin(admin.OSMGeoAdmin):
    list_display = ('__str__', 'dob', 'dod')


# Register your models here.


admin.site.register(SourceMaterial, SourceMaterialAdmin)
admin.site.register(TransationEvents, TransactionAdmin)
admin.site.register(Genre)
admin.site.register(PageImage)
admin.site.register(Person)
admin.site.register(Title)
admin.site.register(Work, WorkAdmin)
admin.site.register(Support)
admin.site.register(Shape)
admin.site.register(Location, LocationAdmin)
admin.site.register(Dealership)
admin.site.register(WorkImage)
admin.site.register(Commission)
admin.site.register(Nationality)
admin.site.register(Movement)
admin.site.register(School)
admin.site.register(SubGenre)
admin.site.register(CurrentLocation)
admin.site.register(LocationType)
