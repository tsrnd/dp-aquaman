from django.shortcuts import HttpResponse


def test(request):
    return HttpResponse(200)
