from django.urls import path
from .views import (
    HomePageView,
    WorkorderListView,
    WorkorderDetailView,
    LogDetailView,
    LogCreateView,
    export_data,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("workorders/", WorkorderListView.as_view(), name="workorder_list"),
    path(
        "workorders/<int:pk>/", WorkorderDetailView.as_view(), name="workorder_detail"
    ),
    path("workorders/<int:pk>/export/", export_data, name="export_data"),
    path("log/<int:pk>/", LogDetailView.as_view(), name="log_detail"),
    path(
        "log/new/<int:workorder_pk>/",
        LogCreateView.as_view(),
        name="log_new",
    ),
]
