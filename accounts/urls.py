from django.urls import path

from .views import LogOutRenderView

urlpatterns = [
    path("logout/", LogOutRenderView.as_view(), name="logout"),
]
