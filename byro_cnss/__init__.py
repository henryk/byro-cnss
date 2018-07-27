from django.apps import AppConfig
from django.utils.translation import ugettext_lazy


class PluginApp(AppConfig):
    name = 'byro_cnss'
    verbose_name = 'byro CNSS plugin'

    class ByroPluginMeta:
        name = ugettext_lazy('byro CNSS plugin')
        author = 'Henryk Plötz'
        description = ugettext_lazy('Byro plugin for CNSS (Clausewitz-Netzwerk für Strategische Studien e.V.)')
        visible = True
        version = '0.0.1'

    def ready(self):
        from . import signals  # NOQA
        from . import models  # NOQA


default_app_config = 'byro_cnss.PluginApp'
