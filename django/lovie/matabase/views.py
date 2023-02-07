from django.shortcuts import render, redirect
from django.contrib import messages # alert/flash messages
from .models import *
from django.db.models import Q  # Q expression
from django.contrib.auth.models import User # registering new member to django User models
from django.contrib.auth import authenticate, login # for logging in


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


# footer fetching
footer = {'stackLen':'', 'linDevLen':'', 'stack':[], 'links':[], 'developer':[]}
footers = Footer.objects.all()
for f in footers:
    if f.category == 'stack':
        footer['stack'].append(f)
    elif f.category == 'links':
        footer['links'].append(f)
    else:
        if f.title.lower() == 'email':
            f.link = f.link.replace('http://', '')
        footer['developer'].append(f)
footer['stackLen'] = len(footer['stack'])
footer['linDevLen'] = len(footer['links']) + len(footer['developer'])


def Tags(movies):
    tags = {}
    for m in movies:
        mags = Mag.objects.filter(magReference=m).values()
        for mg in mags:
            # if movie id existed and tag value not repeat, append the tag list
            if mg['magReference_id'] in tags and mg['mag'] not in tags[mg['magReference_id']]:
                tags[mg['magReference_id']].append(mg['mag'])
            else:
                tags[mg['magReference_id']] = [mg['mag']]
    return tags


def Tag(movie):
    tags = {}
    mags = Mag.objects.filter(magReference=movie).values()
    for mg in mags:
        # if movie id existed and tag value not repeat, append the tag list
        # {'id': 102, 'magReference_id': 730, 'mag': 'action, comedy'}
        sepMag = mg['mag'].split(',')
        if mg['magReference_id'] in tags and mg['mag'] not in tags[mg['magReference_id']]:
            # tags[mg['magReference_id']].append(mg['mag'])
            tags[mg['magReference_id']].append(sepMag)
        else:
            # tags[mg['magReference_id']] = [mg['mag']]
            tags[mg['magReference_id']] = sepMag
    return tags


genres = ['action', 'comedy', 'crime', 'drama', 'horror', 'animated', 'detective', 'romance', 'scienceFiction', 'superNatural', 'war', 'zombie']
def MatabaseHome(request, moviesPar=None):
    movies = Matabase.objects.filter(status='d').order_by('-createdDate')[:10]
    tags = Tags(movies)
    # movies' fetch by status
    # .get('PARAMETER', None) get PARAMETER OR None to ignore error
    if request.GET.get('moviesPar', None) == 'all': 
        movies = Matabase.objects.all()
        Tags(movies)
        context = {'movies': movies, 'genres': genres, 'tags': tags, 'count': count, 'footer': footer}
        return render(request, 'matabase/home.html', context=context)
    elif request.GET.get('moviesPar', None) == 'watched':
        movies = Matabase.objects.filter(status='w')
        Tags(movies)
        context = {'movies': movies, 'genres': genres, 'tags': tags, 'count': count, 'footer': footer}
        return render(request, 'matabase/home.html', context=context)
    elif request.GET.get('moviesPar', None) == 'downloaded':
        movies = Matabase.objects.filter(status='d')
        Tags(movies)
        context = {'movies': movies, 'genres': genres, 'tags': tags, 'count': count, 'footer': footer}
        return render(request, 'matabase/home.html', context=context)
    elif request.GET.get('moviesPar', None) == 'deleted':
        movies = Matabase.objects.filter(status='r')
        Tags(movies)
        context = {'movies': movies, 'genres': genres, 'tags': tags, 'count': count, 'footer': footer}
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
        Tags(movies)
        context = {'movies': movies, 'genres': genres, 'tags': tags, 'count': count, 'footer': footer}
        return redirect('homePage')
    elif request.GET.get('status', None) == 'watched':
        # change status -> watched
        movieId = request.GET.get('id', None)
        item = Matabase.objects.get(id=movieId)
        item.status = 'w'
        item.save()
        messages.info(request, f"{item.title}'s status had changed to watched")
        movies = Matabase.objects.filter(status='w').order_by('-updatedDate')[:10]
        Tags(movies)
        context = {'movies': movies, 'genres': genres, 'tags': tags, 'count': count, 'footer': footer}
        return redirect('homePage')
    elif request.GET.get('status', None) == 'deleted':
        # change status -> deleted
        movieId = request.GET.get('id', None)
        item = Matabase.objects.get(id=movieId)
        item.status = 'r'
        item.save()
        messages.warning(request, f"{item.title}'s status had changed to deleted")
        movies = Matabase.objects.filter(status='r').order_by('-updatedDate')[:10]
        Tags(movies)
        context = {'movies': movies, 'genres': genres, 'tags': tags, 'count': count, 'footer': footer}
        return redirect('homePage')
    if request.method == 'POST':
        # search function
        if 'searchButton' in request.POST:
            formInfo = request.POST.copy()
            searchKeyword = formInfo.get('searchField').strip().replace('  ', ' ')
            if searchKeyword:
                movies = Matabase.objects.filter(Q(title__contains=searchKeyword) | Q(year__exact=searchKeyword))
                Tags(movies)
                context = {'movies': movies, 'genres': genres, 'tags': tags, 'count': count, 'footer': footer}
            elif not searchKeyword and not formInfo.get('titleField') and not formInfo.get('yearField'):
                # search not found condition
                movies = []
                context = {'movies': movies, 'genres': genres, 'tags': tags, 'count': count, 'footer': footer}
        # add record function
        elif 'addButton' in request.POST:
            formInfo = request.POST.copy()
            if formInfo.get('titleField') and formInfo.get('yearField'):
                title = formInfo.get('titleField')
                year = formInfo.get('yearField')
                # check if record existed OR using model UniqueConstraint instead
                existed = Matabase.objects.filter(title__contains=title, year__contains=year)
                if existed:
                    print(existed)
                    messages.warning(request, f'{title} [{year}] existed on database')
                    return redirect('homePage')
                # if not exist, save new record
                record = Matabase()
                record.title = title
                record.year = year
                record.status = formInfo.get('statusField')
                record.save()
                # get last save item's id to save tag(s) in other model
                checked = ['untag']
                for g in genres:
                    if formInfo.get(g):
                        checked.append(formInfo.get(g))
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
                messages.success(request, f'New record [{record.title}] has been saved!')
            else:
                messages.warning(request, 'New record not save, please provide the movie info completely (both title and year)...')
        elif 'loginButton' in request.POST:
            formInfo = request.POST.copy()
            user = authenticate(username=formInfo.get(
                'username'), password=formInfo.get('password'))
            login(request, user)
            return redirect('homePage')
    context = {'movies': movies, 'genres': genres, 'tags': tags, 'count': count, 'footer': footer}
    return render(request, 'matabase/home.html', context=context)


def MatabaseUpdate(request, id):
    if request.user.is_authenticated:
        movie = Matabase.objects.filter(id=id).first()
        tags = Tag(movie)
        if request.method == 'POST':
            updateForm = request.POST.copy()
            if updateForm.get('searchField') != '':
                searchKey = updateForm.get('searchField', None).strip()
                movies = Matabase.objects.filter(title__contains=searchKey)
                tags = Tags(movies)
                context = {'movies': movies, 'genres': genres, 'tags': tags, 'count': count, 'footer': footer}
                return render(request, 'matabase/home.html', context=context)
            else:
                # update record
                movie.title = updateForm.get('titleField', None)
                movie.year = updateForm.get('yearField', None)
                movie.status = updateForm.get('statusField', None)
                movie.save()
                return redirect('homePage')
    else:
        messages.warning(
            request, f'You have no permission to update record, contact your admin for more info.')
    context = {'movie': movie, 'genres': genres, 'tags': tags, 'count': count, 'footer': footer}
    return render(request, 'matabase/update.html', context=context)


def MatabaseDelete(request, id):
    if request.user.is_authenticated:
        movie = Matabase.objects.filter(id=id).first()
        movie.delete()
        messages.warning(request, f'{movie.title} had been deleted.')
    else:
        messages.warning(request, f'You have no permission to delete record, contact your admin for more info.')
    return redirect('homePage')


def Dashboard(request):
    context = {'count': count, 'footer': footer}
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
    context = {'footer': footer}
    return render(request, 'matabase/register.html', context=context)
