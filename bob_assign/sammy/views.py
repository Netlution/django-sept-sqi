from django.shortcuts import render

def new_view(request):
    context = {
        'about_me': 'Ajagun Samuel is an individual driven by passion and dedication, known for his strong commitment to personal growth and excellence. He has built a reputation for his strategic thinking and problem-solving abilities, excelling in various professional fields. Samuel approaches every challenge with a unique perspective, always aiming to innovate and improve.'
    }
    return render(request, 'sammy/about.html', context)
