from django.views.generic import TemplateView
from .models import About

class AboutPageView(TemplateView):
    template_name = "about/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.first()  # Fetch the first About instance
        return context
