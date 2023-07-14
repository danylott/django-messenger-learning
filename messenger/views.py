from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic

from messenger.models import Message


def home(request: HttpRequest) -> HttpResponse:
    num_messages = Message.objects.count()  # models

    context = {
        "num_messages": num_messages,
        "session_marco": request.session.get("marco", "polo"),
    }

    return render(
        request,
        "messenger/home.html",
        context=context,
    )


def set_session(request: HttpRequest) -> HttpResponse:
    request.session["marco"] = "Not Polo!"
    return HttpResponse("Set session!")


class MessageListView(generic.DetailView):
    model = Message


class MessageDetailView(generic.DetailView):
    model = Message
