import os
from django.conf import settings
from django.views.generic import TemplateView
from django.utils.html import urlize


class HomeView(TemplateView):
    template_name='home.html'


class AboutView(TemplateView):
    template_name='about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['readme'] = urlize(open(os.path.join(settings.BASE_DIR, 'README.rst')).read()).replace('\n', '<br>')
        return context


class ContactView(TemplateView):
    template_name='contact.html'

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['contact'] = urlize(open(os.path.join(settings.BASE_DIR, 'kb/contact.ttl')).read()).replace('\n', '<br>')
        return context
