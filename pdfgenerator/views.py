from django.http import HttpResponse


def generate_pdf(request):
    # pdf generation code goes here
    return HttpResponse("Your pdf has been generated!")
