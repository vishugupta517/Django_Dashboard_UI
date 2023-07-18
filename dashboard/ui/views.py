import json
import os

from django.conf import settings
from django.shortcuts import render

# Create your views here.

managementjson = os.path.join(settings.MEDIA_ROOT, "management.json")


def dashboardScreen(request):
    try:
        with open(managementjson) as f:
            data = json.load(f)
    except:
        data = {}

    jsonData = json.dumps(data)

    context = {"jsonData": jsonData}
    context.update(data)

    return render(request, "home.html", context)
