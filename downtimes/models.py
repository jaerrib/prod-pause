from django.conf import settings
from django.db import models
from django.urls import reverse


class Workorder(models.Model):
    customer_name = models.CharField(max_length=100)
    assembly_number = models.CharField(max_length=100)
    part_number = models.CharField(max_length=100)
    lot_number = models.CharField(max_length=100)
    creator = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.lot_number

    def get_absolute_url(self):
        return reverse("workorder_detail", kwargs={"pk": self.pk})


class Log(models.Model):
    workorder = models.ForeignKey("Workorder", on_delete=models.CASCADE)
    date = models.DateField()
    shift = models.IntegerField()
    down_time = models.TimeField()
    restart_time = models.TimeField()
    problem = models.TextField()
    root_cause = models.TextField()
    corrective_action = models.TextField()
    impact = models.TextField()
    initiator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return (
            self.workorder.assembly_number
            + "-"
            + self.workorder.lot_number
            + "-Entry"
            + str(self.pk)
        )

    def get_absolute_url(self):
        return reverse("log_detail", kwargs={"pk": self.pk})
