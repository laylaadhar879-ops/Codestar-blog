from django.http import HttpResponse

# Blog page view
def blog(request):
    return HttpResponse("Welcome to Codestar Blog!")
