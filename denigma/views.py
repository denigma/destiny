from django.views.generic import TemplateView

from utils.views import LoadView


class HomeView(TemplateView):
    template_name = 'home.html'


class AboutView(LoadView):
    template_name='about.html'
    file_name = 'README.rst'


class ContactView(LoadView):
    template_name='contact.html'
    file_name = 'kb/contact.ttl'