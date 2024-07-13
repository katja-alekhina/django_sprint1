from django.shortcuts import render


def about(request):
    context = {}
    template = 'pages/about.html'
    return render(request, template, context)


def rules(request):
    context = {}
    template = 'pages/rules.html'
    return render(request, template, context)
