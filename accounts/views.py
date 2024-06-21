from django.urls import reverse_lazy
from django.views.generic import TemplateView


class LogOutRenderView(TemplateView):
    template_name = reverse_lazy("home")
