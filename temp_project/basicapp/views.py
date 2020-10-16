from django.shortcuts import render

# Create your views here.
def index(request):
    data = {'text':'hello world', 'number':100}
    return render(request, 'basicapp/index.html', data)

def other(request):
    return render(request, 'basicapp/other.html')

def relative(request):
    return render(request, 'basicapp/rel_url_template.html')
