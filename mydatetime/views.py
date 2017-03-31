from django.http import HttpResponse, Http404
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
from books.models import Book
# Create your views here.

def hello(request):
    return HttpResponse("Hello django")

def current_time(request):
    now = datetime.datetime.now()
    #tmpl = Template("<html><body>It is now i {{current_time}}</body></html>")
    #tmpl = get_template("current_time.html")
    #ctx = Context({"current_time": now})
    #assert False
    #response = tmpl.render(ctx)
    #return HttpResponse(response)
    return render(request, "current_time_extend.html", {"current_time": now, "site": "{{site2}}"})

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    target = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render(request, "hours_ahead_extend.html", {"hour_offset": offset, "next_time": target})

def display_meta(request):
    values = request.META.items()
    #values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def search_form(request):
    return render(request, "search_form.html")

def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        return render(request, 'search_results.html',
                      {'books': books, 'query': q})
    else:
        return render(request, 'search_form.html', {'error': True})