from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Api

def index(request):
    latest_api_list = Api.objects.order_by('-api_add_date')[:5]
    context = {'latest_api_list':latest_api_list}
    return render(request, 'apis/index.html', context)

def hello(request):
    #api = get_object_or_404(Api, pk=api_id)
    return render(request, 'apis/hello.html')

def detail(request, api_id):
    api = get_object_or_404(Api, pk=api_id)
    return render(request, 'apis/detail.html', {'api':api})

def results(request, api_id):
    response = "You're looking at the result of api %s."
    return HttpResponse(response % api_id)
