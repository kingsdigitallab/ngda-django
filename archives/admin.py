from django.contrib.gis import admin


from archives.models import SourceMaterial, TransationEvents,\
    Person, Title, Work, Support, Shape, Location


class LocationAdmin(admin.OSMGeoAdmin):
    openlayers_url = 'https://openlayers.org/api/2.13.1/OpenLayers.js'


# Register your models here.


admin.site.register(SourceMaterial)
admin.site.register(TransationEvents)
admin.site.register(Person)
admin.site.register(Title)
admin.site.register(Work)
admin.site.register(Support)
admin.site.register(Shape)
admin.site.register(Location, LocationAdmin)
