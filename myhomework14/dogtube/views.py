from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from dogtube.models import Video


def index(request: HttpRequest) -> HttpResponse:
    qs = Video.objects.all()
    return render(request,
                  "dogtube/index.html",
                  {
                      "video_list": qs,
                  },
                  )

