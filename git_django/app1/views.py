from django.shortcuts import render

posts = [
    {
        'author': 'Veit',
        'title': 'Günstig Leberkäs',
        'content': 'Heute gibt es im Rewe leberkäse 100g für 50 cent',
        'date': '21.August.2022'
    },

    {
        'author': 'Helli',
        'title': 'Metal rocks',
        'content': 'Auf nach Wacken!',
        'date': '22.August.2022'
    },
    {
        'author': 'FettEX',
        'title': 'Abnehmen',
        'content': 'whatever it takes',
        'date': '11.September.2022 12.37 von pycharm'
    },

]

def home(request):
    return render(request, 'app1/home.html')

def about(request):
    context = {
        'posts': posts
    }
    return render(request, 'app1/about.html', context)