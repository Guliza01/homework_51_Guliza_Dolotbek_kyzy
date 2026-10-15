from django.shortcuts import render
from webapp.cat_db import catdb


def index_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        catdb.context['name'] = request.POST.get('name')
        return render(request, 'cat_stats.html', catdb.context)


def cat_stats_view(request):
    if request.method == 'GET':
        return render(request, 'cat_stats.html', catdb.context)
    elif request.method == 'POST':
        action = request.POST.get('action')
        catdb.context['name'] = request.POST.get('name')

        if action == 'sleep':
            catdb.put_to_bed()
        elif action == 'feed':
            catdb.feed_the_cat()
        elif action == 'play':
            catdb.play_with_the_cat()

        return render(request, 'cat_stats.html', catdb.context)
