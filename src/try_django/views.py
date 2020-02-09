
from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    return render(request, "home.html", {"title": "Hello There..."})


def about_page(request):
    return render(request, "about.html", {"title": "About Us"})


def contact_page(request):
    return render(request, "contact.html", {"title": "Contact"})


def example_page(request):
    context = {"title": "Example"}
    template_name = "base.html"
    template_obj = get_template(template_name)
    rendered_item = template_obj.render(context)
    return HttpResponse(rendered_item)
