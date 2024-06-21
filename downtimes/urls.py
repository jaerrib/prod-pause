from django.urls import path
from .views import (
    HomePageView,
    WorkorderListView,
    WorkorderDetailView,
    LogDetailView,
    LogCreateView,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("workorders/", WorkorderListView.as_view(), name="workorder_list"),
    path(
        "workorders/<int:pk>/", WorkorderDetailView.as_view(), name="workorder_detail"
    ),
    path("log/<int:pk>/", LogDetailView.as_view(), name="log_detail"),
    path(
        "log/new/<int:workorder_pk>/",
        LogCreateView.as_view(),
        name="log_new",
    ),
]
