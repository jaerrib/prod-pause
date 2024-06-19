import csv

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import (
    LogCreateForm,
)
from .models import Log, Workorder


class HomePageView(TemplateView):
    template_name = "base.html"


class WorkorderListView(LoginRequiredMixin, ListView):
    model = Workorder
    template_name = "workorders.html"   


class WorkorderDetailView(LoginRequiredMixin, DetailView):
    model = Workorder
    template_name = "workorder_detail.html"


class LogDetailView(LoginRequiredMixin, DetailView):
    model = Log
    template_name = "log_detail.html"


class LogCreateView(LoginRequiredMixin, CreateView):
    model = Log
    form_class = LogCreateForm
    template_name = "log_new.html"
    context_object_name = "workorder"
    pk_url_kwarg = "workorder_pk"

    def get_redirect_url(self, param):
        return reverse_lazy("log_list_detail", kwargs={"param": param})

    def get_queryset(self):
        return Workorder.objects.filter(pk=self.kwargs["workorder_pk"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = LogCreateForm()
        context["workoder"] = Workorder.objects.get(pk=self.kwargs["workorder_pk"])
        return context

    def form_valid(self, form):
        form.instance.workorder = Workorder.objects.get(pk=self.kwargs["workorder_pk"])
        form.instance.creator = self.request.user
        return super().form_valid(form)


# def export_data(request):
#     query_set = ToDo.objects.filter(creator=request.user.pk).order_by(
#         "todo_list__title"
#     )
#     response = HttpResponse(
#         content_type="text/csv",
#         headers={"Content-Disposition": 'attachment; filename="exported_data.csv"'},
#     )
#     writer = csv.writer(response)

#     writer.writerow(
#         [
#             "Title",
#             "Details",
#             "Important",
#             "Urgent",
#             "Due Date",
#             "Completed",
#             "ToDo List",
#         ]
#     )
#     for item in query_set:
#         writer.writerow(
#             [
#                 item.title,
#                 item.details,
#                 item.important,
#                 item.urgent,
#                 item.due_date,
#                 item.completed,
#                 item.todo_list,
#             ]
#         )

#     return response
