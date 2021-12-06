from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from cutedog.models import Video

# Class Based View (CBV)
index = ListView.as_view(model=Video, template_name="cutedog/index.html")

def video_detail(request: HttpRequest, pk: int) -> HttpResponse:
    video = Video.objects.get(pk=pk)
    return render(
        request,
        "cutedog/video_detail.html",
        {
            "video": video,
        },
    )


