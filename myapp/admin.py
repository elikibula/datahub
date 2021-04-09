from django.contrib import admin

from myapp.models import Lewenilotu, Matasiga, Veitokani, Valenilotu, Veitosoyaki, Veivakalotutaki, Bulararaba


@admin.register(Lewenilotu)
class LewenilotuAdmin(admin.ModelAdmin):
    list_display = ('lewenilotu', 'phone_contact', 'valenilotu')

    pass


@admin.register(Matasiga)
class MatasigaAdmin(admin.ModelAdmin):
    list_display = ('matasiga', 'liuliu_ni_matasiga', 'valenilotu')

    pass


@admin.register(Veitokani)
class VeitokaniAdmin(admin.ModelAdmin):
    
    pass


@admin.register(Valenilotu)
class ValenilotuAdmin(admin.ModelAdmin):

    pass


@admin.register(Veitosoyaki)
class VeitosoyakiAdmin(admin.ModelAdmin):

    pass


@admin.register(Veivakalotutaki)
class VeivakalotutakiAdmin(admin.ModelAdmin):
    
    pass


@admin.register(Bulararaba)
class BulararabaAdmin(admin.ModelAdmin):

    pass


# Register your models here.
