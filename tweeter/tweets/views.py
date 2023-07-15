from django.shortcuts import render

posts = [
    {
        'author': 'ed',
        'title': 'tweet1',
        'content': ' meeps',
        'date': 'today'
    },
    {
        'author': 'irma',
        'title': 'tweet2',
        'content': ' moops',
        'date': 'tomorrow'
    }
]


def home(request):
    context = {
        'title': 'latest tweets',
        'posts': posts
    }
    return render(request, 'tweets/home.html', context)


def away(request):
    return render(request, 'tweets/away.html')
