from django.shortcuts import render


def start(request):
    return render(request, 'admin/index.html')