from django.http import Http404
from django.shortcuts import render
# Create your views here.
from .models import Project, Api
#from django.http import HttpResponse

def index(request):
    latest_project_list = Project.objects.order_by('-add_project_date')[:5]
    context = {'latest_project_list':latest_project_list}
    return render(request, 'apis/index.html', context)

    #latest_project_list = Project.objects.order_by('-add_project_date')[:5]
    #output = ', '.join([p.project_name for p in latest_project_list])
    #return HttpResponse(output)

def hello(request):
    #api = get_object_or_404(Api, pk=api_id)
    return render(request, 'apis/hello.html')

def css(request):
    #api = get_object_or_404(Api, pk=api_id)
    return render(request, 'apis/layui/css/layui.css')

def js(request):
    #api = get_object_or_404(Api, pk=api_id)
    return render(request, 'apis/layui/layui.js')


def detail(request, project_id):
    #api = get_object_or_404(Api, pk=project_id)
    #print(api)
    #return render(request, 'apis/detail.html', {'api':api})

    try:
        project = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        raise Http404("Project does not exist")
    return render(request, 'apis/detail.html', {'project': project})

def api(request, project_id):
    try:
        api = Api.objects.get(pk=project_id)
    except Project.DoesNotExist:
        raise Http404("Api does not exist")
    return render(request, 'apis/api.html', {'api': api})
    

def results(request, project_id):
    response = "You're looking at the result of api %s."
    return HttpResponse(response % project_id)
