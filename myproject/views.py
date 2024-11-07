from django.shortcuts import render

def menu_view(request):
    return render(request, 'menu.html', {
        'modules': [
            #{'name': 'Module 1', 'url': '/module1/'},
            {'name': 'Module 2', 'url': '/module2/'},
        ]
    })