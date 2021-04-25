from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from stackapi import StackAPI
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.decorators.cache import cache_page

@cache_page(30)
def index(request):
    SITE = StackAPI('stackoverflow')
    object_list = SITE.fetch('questions',min=20, tagged='python', sort='votes', )
    object = [x for x in object_list['items']]
    paginator = Paginator(object, 50)
    page_num  = request.GET.get('page')
    page = paginator.get_page(page_num)

    context = {
        "count": paginator.count,
        "page": page
    }
    return render(request, 'index.html',context)