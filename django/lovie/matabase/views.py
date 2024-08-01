from django.shortcuts import render, redirect
from django.contrib import messages # alert/flash messages
from .models import *
from django.db.models import Q  # Q expression
from django.contrib.auth.models import User # registering new member to django User models
from django.contrib.auth import authenticate, login # for logging in
from django.core.paginator import Paginator # Paginator

'''
# db record count
watched = Matabase.objects.filter(status='w').count()
downloaded = Matabase.objects.filter(status='d').count()
deleted = Matabase.objects.filter(status='r').count()
totalMovies = watched + downloaded + deleted
if totalMovies == 0:
    watAsPercentage = 0
    dowAsPercentage = 0
    delAsPercentage = 0
else:
    watAsPercentage = round(watched*100 / totalMovies)
    dowAsPercentage = round(downloaded*100 / totalMovies)
    delAsPercentage = round(deleted*100 / totalMovies)
count = {
    'all':totalMovies, 'downloaded':downloaded, 'watched':watched, 'deleted':deleted,
    'dowAsPercentage': dowAsPercentage, 'watAsPercentage': watAsPercentage, 'delAsPercentage': delAsPercentage
}
'''
def MatabaseHome(request, moviesPar=None):
    # db record count
    watched = Matabase.objects.filter(status='w').count()
    downloaded = Matabase.objects.filter(status='d').count()
    deleted = Matabase.objects.filter(status='r').count()
    totalMovies = watched + downloaded + deleted
    count = {
        'all':totalMovies, 'downloaded':downloaded, 'watched':watched, 'deleted':deleted
    }
    def Tag(movies):
        for m in movies:
            movies.test = 'testField'
            mags = Mag.objects.filter(magReference=m).values()
            for mg in mags:
                # if movie id existed and tag value not repeat, append the tag list
                if mg['magReference_id'] in tags and mg['mag'] not in tags[mg['magReference_id']]:
                    tags[mg['magReference_id']].append(mg['mag'])
                else:
                    tags[mg['magReference_id']] = [mg['mag']]
        return tags
    genres = ['action', 'comedy', 'crime', 'drama', 'horror', 'animated', 'detective', 'romance', 'scienceFiction', 'superNatural', 'war', 'zombie']
    movies = Matabase.objects.filter(status='d').order_by('-createdDate')[:10]
    tags = {}
    Tag(movies)
    # movies' fetch by status
    if request.GET.get('moviesPar', None) == 'all':
        if request.method == 'POST':
            if 'searchButton' in request.POST:
                formInfo = request.POST.copy()
                searchKeyword = formInfo.get('searchField').strip().replace('  ', ' ')
                if searchKeyword:
                    movies = Matabase.objects.filter(Q(title__contains=searchKeyword) | Q(year__exact=searchKeyword))
                    Tag(movies)
                    context = {'movies': movies, 'genres': genres, 'tags': tags, 'count': count}
                elif not searchKeyword and not formInfo.get('titleField') and not formInfo.get('yearField'):
                    movies = []
                    context = {'movies': movies, 'genres': genres, 'tags': tags, 'count': count}
            return render(request, 'matabase/home.html', context=context)
    # .get('PARAMETER', None) get PARAMETER OR None to ignore error
        movies = Matabase.objects.all()
        paginator = Paginator(movies, 10)
        page = request.GET.get('page')
        movies = paginator.get_page(page)
        Tag(movies)
        context = {'movies': movies, 'genres': genres, 'tags': tags, 'count': count, 'page': 'all'}
        return render(request, 'matabase/home.html', context=context)
    elif request.GET.get('moviesPar', None) == 'watched':
        if request.method == 'POST':
            if 'searchButton' in request.POST:
                formInfo = request.POST.copy()
                searchKeyword = formInfo.get('searchField').strip().replace('  ', ' ')
                if searchKeyword:
                    movies = Matabase.objects.filter((Q(title__contains=searchKeyword) | Q(year__exact=searchKeyword)) & Q(status__exact='w'))
                    Tag(movies)
                    context = {'movies': movies, 'genres': genres, 'tags': tags, 'count': count}
                elif not searchKeyword and not formInfo.get('titleField') and not formInfo.get('yearField'):
                    movies = []
                    context = {'movies': movies, 'genres': genres, 'tags': tags, 'count': count}
            return render(request, 'matabase/home.html', context=context)
        movies = Matabase.objects.filter(status='w')
        paginator = Paginator(movies, 10)
        page = request.GET.get('page')
        movies = paginator.get_page(page)
        Tag(movies)
        context = {'movies': movies, 'genres': genres, 'tags': tags, 'count': count, 'page': 'watched'}
        return render(request, 'matabase/home.html', context=context)
    elif request.GET.get('moviesPar', None) == 'downloaded':
        if request.method == 'POST':
            if 'searchButton' in request.POST:
                formInfo = request.POST.copy()
                searchKeyword = formInfo.get('searchField').strip().replace('  ', ' ')
                if searchKeyword:
                    movies = Matabase.objects.filter((Q(title__contains=searchKeyword) | Q(year__exact=searchKeyword)) & Q(status__exact='d'))
                    Tag(movies)
                    context = {'movies': movies, 'genres': genres, 'tags': tags, 'count': count}
                elif not searchKeyword and not formInfo.get('titleField') and not formInfo.get('yearField'):
                    movies = []
                    context = {'movies': movies, 'genres': genres, 'tags': tags, 'count': count}
            return render(request, 'matabase/home.html', context=context)
        movies = Matabase.objects.filter(status='d')
        paginator = Paginator(movies, 10)
        page = request.GET.get('page')
        movies = paginator.get_page(page)
        Tag(movies)
        context = {'movies': movies, 'genres': genres, 'tags': tags, 'count': count, 'page': 'downloaded'}
        return render(request, 'matabase/home.html', context=context)
    elif request.GET.get('moviesPar', None) == 'deleted':
        if request.method == 'POST':
            if 'searchButton' in request.POST:
                formInfo = request.POST.copy()
                searchKeyword = formInfo.get('searchField').strip().replace('  ', ' ')
                if searchKeyword:
                    movies = Matabase.objects.filter((Q(title__contains=searchKeyword) | Q(year__exact=searchKeyword)) & Q(status__exact='r'))
                    Tag(movies)
                    context = {'movies': movies, 'genres': genres, 'tags': tags, 'count': count}
                elif not searchKeyword and not formInfo.get('titleField') and not formInfo.get('yearField'):
                    movies = []
                    context = {'movies': movies, 'genres': genres, 'tags': tags, 'count': count}
            return render(request, 'matabase/home.html', context=context)
        movies = Matabase.objects.filter(status='r')
        paginator = Paginator(movies, 10)
        page = request.GET.get('page')
        movies = paginator.get_page(page)
        Tag(movies)
        context = {'movies': movies, 'genres': genres, 'tags': tags, 'count': count, 'page': 'deleted'}
        return render(request, 'matabase/home.html', context=context)
    # status links action
    if request.GET.get('status', None) == 'downloaded':
        # change status -> downloaded
        movieId = request.GET.get('id', None)
        item = Matabase.objects.get(id=movieId)
        item.status = 'd'
        item.save()
        messages.success(request, f"{item.title}'s status had changed to downloaded")
        movies = Matabase.objects.filter(status='d').order_by('-updatedDate')[:10]
        Tag(movies)
        context = {'movies': movies, 'genres': genres, 'tags': tags, 'count': count}
        return redirect('homePage')
    elif request.GET.get('status', None) == 'watched':
        # change status -> watched
        movieId = request.GET.get('id', None)
        item = Matabase.objects.get(id=movieId)
        item.status = 'w'
        item.save()
        messages.info(request, f"{item.title}'s status had changed to watched")
        movies = Matabase.objects.filter(status='w').order_by('-updatedDate')[:10]
        Tag(movies)
        context = {'movies': movies, 'genres': genres, 'tags': tags, 'count': count}
        return redirect('homePage')
    elif request.GET.get('status', None) == 'deleted':
        # change status -> deleted
        movieId = request.GET.get('id', None)
        item = Matabase.objects.get(id=movieId)
        item.status = 'r'
        item.save()
        messages.warning(request, f"{item.title}'s status had changed to deleted")
        movies = Matabase.objects.filter(status='r').order_by('-updatedDate')[:10]
        Tag(movies)
        context = {'movies': movies, 'genres': genres, 'tags': tags, 'count': count}
        return redirect('homePage')
    if request.method == 'POST':
        if 'searchButton' in request.POST:
            formInfo = request.POST.copy()
            if formInfo.get('searchField'):
                movies = Matabase.objects.filter(Q(title__contains=formInfo.get('searchField')) | Q(year__exact=formInfo.get('searchField')))
                Tag(movies)
                context = {'movies': movies, 'genres': genres, 'tags': tags}
            elif not formInfo.get('searchField') and not formInfo.get('titleField') and not formInfo.get('yearField'):
                # search not found condition
                movies = []
                context = {'movies': movies, 'genres': genres, 'tags': tags, 'count': count}
        elif 'addButton' in request.POST:
            formInfo = request.POST.copy()
            if formInfo.get('titleField') and formInfo.get('yearField'):
                record = Matabase()
                record.title = formInfo.get('titleField')
                record.year = formInfo.get('yearField')
                record.status = formInfo.get('statusField')
                record.save()
                # get last save item's id to save tag(s) in other model
                checked = ['untag']
                for g in genres:
                    if formInfo.get(g):
                        checked.append(formInfo.get(g))
                        print(formInfo.get(g))
                if len(checked)>1:
                    checked.remove('untag')
                # lastItem = Matabase.objects.get(title = formInfo.get('titleField'))
                lastItem = Matabase.objects.latest('id')
                for c in checked:
                    # save tag(s) into model
                    mag = Mag()
                    mag.magReference = lastItem
                    mag.mag = c
                    mag.save()
                    print(lastItem.title, c)
                messages.success(request, f'New record [{record.title}] has been saved!')
            else:
                messages.warning(request, 'New record not save, please provide the movie info completely (both title and year)...')
        elif 'loginButton' in request.POST:
            formInfo = request.POST.copy()
            user = authenticate(username=formInfo.get(
                'username'), password=formInfo.get('password'))
            login(request, user)
            return redirect('homePage')
    context = {'movies': movies, 'genres': genres, 'tags': tags, 'count': count}
    return render(request, 'matabase/home.html', context=context)

def Dashboard(request):
    watched = Matabase.objects.filter(status='w').count()
    downloaded = Matabase.objects.filter(status='d').count()
    deleted = Matabase.objects.filter(status='r').count()
    totalMovies = watched + downloaded + deleted
    if totalMovies == 0:
        watchedPercentage = 0
        downloadedPercentage = 0
        deletedPercentage = 0
    else:
        watchedPercentage = round(watched*100 / totalMovies)
        downloadedPercentage = round(downloaded*100 / totalMovies)
        deletedPercentage = round(deleted*100 / totalMovies)
    context = {'totalMovies': totalMovies, 'watched': watched, 'downloaded': downloaded, 'deleted': deleted, 'watchedPercentage': watchedPercentage, 'downloadedPercentage': downloadedPercentage, 'deletedPercentage': deletedPercentage}
    return render(request, 'matabase/dash.html', context=context)

def Register(request):
    if 'loginButton' in request.POST:
        formInfo = request.POST.copy()
        user = authenticate(username=formInfo.get(
            'username'), password=formInfo.get('password'))
        login(request, user)
        return redirect('homePage')
    elif 'registerButton' in request.POST:
    # if request.method == 'POST':
        formInfo = request.POST.copy()
        if formInfo.get('password') != formInfo.get('confirmPassword'):
            return redirect('registerPage')
        newUser = User()
        newUser.first_name = formInfo.get('firstname')
        newUser.last_name = formInfo.get('lastname')
        newUser.email = formInfo.get('email')
        newUser.username = formInfo.get('username')
        newUser.set_password(formInfo.get('password'))
        newUser.save()
        user = authenticate(username=formInfo.get('username'), password=formInfo.get('password'))
        login(request, user)
        return redirect('homePage')
    context = {}
    return render(request, 'matabase/register.html', context=context)
