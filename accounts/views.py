from django.urls import reverse_lazy
from django.views.generic import TemplateView

from .forms import CustomUserCreationForm




class LogOutRenderView(TemplateView):
    template_name = reverse_lazy('home')
