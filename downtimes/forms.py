from django import forms
from django.forms import ModelForm

from .models import Log, Workorder, ErrorCode


class DateInput(forms.DateInput):
    input_type = "date"


class TimeInput(forms.TimeInput):
    input_type = "time"


class LogCreateForm(ModelForm):
    error_code = forms.ModelChoiceField(queryset=ErrorCode.objects.all())

    class Meta:
        model = Log
        fields = [
            "date",
            "shift",
            "down_time",
            "restart_time",
            "error_code",
            "problem",
            "root_cause",
            "corrective_action",
            "impact",
        ]

        widgets = {
            "date": DateInput(),
            "down_time": TimeInput(),
            "restart_time": TimeInput(),
        }


class LogUpdateForm(ModelForm):
    error_code = forms.ModelChoiceField(queryset=ErrorCode.objects.all())

    class Meta:
        model = Log
        fields = [
            "date",
            "shift",
            "down_time",
            "restart_time",
            "error_code",
            "problem",
            "root_cause",
            "corrective_action",
            "impact",
        ]
        widgets = {
            "date": DateInput(),
            "down_time": TimeInput(),
            "restart_time": TimeInput(),
        }


class WorkorderCreateForm(ModelForm):
    class Meta:
        model = Workorder
        fields = [
            "customer_name",
            "assembly_number",
            "part_number",
            "lot_number",
        ]


class WorkorderUpdateForm(ModelForm):
    class Meta:
        model = Workorder
        fields = [
            "customer_name",
            "assembly_number",
            "part_number",
            "lot_number",
        ]
