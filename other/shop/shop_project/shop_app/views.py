from django.db.models import Count
from django.shortcuts import render
from shop_app.models import Visit

# Create your views here.


def index(request):
    if request.method == 'GET':
            Visit.objects.create(url=request.path)
            urls = Visit.objects.values('url').distinct().annotate(count=Count('id')).order_by('count').reverse()
            return render(request, 'shop_app/index.html', {'urls': urls}, )