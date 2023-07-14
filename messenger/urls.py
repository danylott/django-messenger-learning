from django.urls import path

from .views import home, MessageListView, MessageDetailView, set_session

urlpatterns = [
    path("home/", home, name="home"),
    path(
        "set_session/",
        set_session,
        name="set-session",
    ),
    path("messages/", MessageListView.as_view(), name="message-list"),
    path("messages/<int:pk>/", MessageDetailView.as_view(), name="message-detail"),
]

app_name = "messenger"
