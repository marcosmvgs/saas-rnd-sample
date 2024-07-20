from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit


def home_view(request, *args, **kwargs):
    return about_view(request, *args, **kwargs)


def about_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    
    try:
        percent = f"{round((page_qs.count() * 100.0) / qs.count(), 2),} %"
    except:
        percent = 0

    my_title = "My Page"
    my_context = {
        'page_title': my_title,
        'page_visit_count': page_qs.count(),
        'percent': percent,
        'total_visit_count': qs.count()
    }
    PageVisit.objects.create(path=request.path)
    return render(request, template_name="home.html", context=my_context)
