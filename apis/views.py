from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Project, Api

def index(request):
    latest_project_list = Api.objects.order_by('-add_project_date')[:5]
    context = {'latest_project_list':latest_project_list}
    return render(request, 'apis/index.html', context)

def hello(request):
    #api = get_object_or_404(Api, pk=api_id)
    return render(request, 'apis/hello.html')

def detail(request, project_id):
    api = get_object_or_404(Api, pk=project_id)
    return render(request, 'apis/detail.html', {'api':api})

def results(request, project_id):
    response = "You're looking at the result of api %s."
    return HttpResponse(response % project_id)
