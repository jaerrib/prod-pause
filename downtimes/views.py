import csv

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView

from .forms import (
    LogCreateForm,
)
from .models import Log, Workorder


class HomePageView(TemplateView):
    template_name = "home.html"


class WorkorderListView(LoginRequiredMixin, ListView):
    model = Workorder
    template_name = "workorders.html"


class WorkorderDetailView(LoginRequiredMixin, DetailView):
    model = Workorder
    template_name = "workorder_detail.html"
    context_object_name = "log_list"
    pk_url_kwarg = "pk"

    def get_queryset(self):
        return Workorder.objects.filter(pk=self.kwargs["pk"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        workorder = self.get_object()
        context["log_list"] = Log.objects.filter(workorder=workorder).order_by("-date", "-down_time")
        context["workorder"] = workorder
        context["workorder_pk"] = workorder.pk
        return context


class LogDetailView(LoginRequiredMixin, DetailView):
    model = Log
    template_name = "log_detail.html"


class LogCreateView(LoginRequiredMixin, CreateView):
    model = Log
    form_class = LogCreateForm
    template_name = "log_new.html"
    context_object_name = "workorder"
    pk_url_kwarg = "workorder_pk"

    def get_success_url(self):
        workorder_pk = self.object.workorder.pk
        return reverse("workorder_detail", kwargs={"pk": workorder_pk})

    def get_redirect_url(self, param):
        return reverse_lazy("workorder_detail", kwargs={"param": param})

    def get_queryset(self):
        return Workorder.objects.filter(pk=self.kwargs["workorder_pk"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = LogCreateForm()
        context["workorder"] = Workorder.objects.get(pk=self.kwargs["workorder_pk"])
        context["workorder_pk"] = self.kwargs["workorder_pk"]
        return context

    def form_valid(self, form):
        form.instance.workorder = Workorder.objects.get(pk=self.kwargs["workorder_pk"])
        form.instance.initiator = self.request.user
        return super().form_valid(form)


def export_data(request, pk):
    query_set = Log.objects.filter(workorder=pk)
    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="exported_data.csv"'},
    )
    writer = csv.writer(response)
    if len(query_set) > 0:
        writer.writerow(
            ["Customer Name", "Assembly Number", "Part Number", "Lot Number"]
        )
        workorder = Workorder.objects.get(id=pk)
        writer.writerow(
            [
                workorder.customer_name,
                workorder.assembly_number,
                workorder.part_number,
                workorder.lot_number,
            ]
        )
        writer.writerow(
            [
                "Date",
                "Shift",
                "Down Time",
                "Restart Time",
                "Problem",
                "Corrective Action",
                "Impact",
                "Initiator",
            ]
        )
        for item in query_set:
            writer.writerow(
                [
                    item.date,
                    item.shift,
                    item.down_time,
                    item.restart_time,
                    item.problem,
                    item.corrective_action,
                    item.impact,
                    item.initiator,
                ]
            )
    return response
