from django.shortcuts import render, redirect
from django.contrib import messages # alert/flash messages
from .models import *
from django.db.models import Q # Q expression
from django.contrib.auth.models import User # registering new member to django User models
from django.contrib.auth import authenticate, login # for logging in
from django.core.paginator import Paginator # Paginator




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
    movies = Matabase.objects.filter(status='d').order_by('createdDate', 'title')
    paginator = Paginator(movies, 10) 
    page = request.GET.get('page')
    movies = paginator.get_page(page)
    # tags = Tags(movies)
    # movies' fetch by status
    # .get('PARAMETER', None) get PARAMETER OR None to ignore error
    if request.GET.get('moviesPar', None) == 'all': 
        # pagination
        # conValPaginator = Paginator(conValForms, 2)
        # conValPage = request.GET.get('page')
        # conValForm = conValPaginator.get_page(conValPage)
        movies = Matabase.objects.all()
        paginator = Paginator(movies, 10) 
        page = request.GET.get('page')
        movies = paginator.get_page(page)
        # show "Page # of TOTAL PAGE"
        # Tags(movies)
        context = {'movies': movies, 'genres': genres, 'count': count, 'footer': footer, 'page': 'all'}
        return render(request, 'matabase/home.html', context=context)
    elif request.GET.get('moviesPar', None) == 'watched':
        movies = Matabase.objects.filter(status='w')
        paginator = Paginator(movies, 10) 
        page = request.GET.get('page')
        movies = paginator.get_page(page)
        # Tags(movies)
        context = {'movies': movies, 'genres': genres, 'count': count, 'footer': footer, 'page': 'watched'}
        return render(request, 'matabase/home.html', context=context)
    elif request.GET.get('moviesPar', None) == 'downloaded':
        movies = Matabase.objects.filter(status='d')
        paginator = Paginator(movies, 10) 
        page = request.GET.get('page')
        movies = paginator.get_page(page)
        # Tags(movies)
        context = {'movies': movies, 'genres': genres, 'count': count, 'footer': footer, 'page': 'downloaded'}
        return render(request, 'matabase/home.html', context=context)
    elif request.GET.get('moviesPar', None) == 'deleted':
        movies = Matabase.objects.filter(status='r')
        paginator = Paginator(movies, 10) 
        page = request.GET.get('page')
        movies = paginator.get_page(page)
        # Tags(movies)
        context = {'movies': movies, 'genres': genres, 'count': count, 'footer': footer, 'page': 'deleted'}
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
        # Tags(movies)
        context = {'movies': movies, 'genres': genres, 'count': count, 'footer': footer}
        return redirect('homePage')
    elif request.GET.get('status', None) == 'watched':
        # change status -> watched
        movieId = request.GET.get('id', None)
        item = Matabase.objects.get(id=movieId)
        item.status = 'w'
        item.save()
        messages.info(request, f"{item.title}'s status had changed to watched")
        movies = Matabase.objects.filter(status='w').order_by('-updatedDate')[:10]
        # Tags(movies)
        context = {'movies': movies, 'genres': genres, 'count': count, 'footer': footer}
        return redirect('homePage')
    elif request.GET.get('status', None) == 'deleted':
        # change status -> deleted
        movieId = request.GET.get('id', None)
        item = Matabase.objects.get(id=movieId)
        item.status = 'r'
        item.save()
        messages.warning(request, f"{item.title}'s status had changed to deleted")
        movies = Matabase.objects.filter(status='r').order_by('-updatedDate')[:10]
        # Tags(movies)
        context = {'movies': movies, 'genres': genres, 'count': count, 'footer': footer}
        return redirect('homePage')
    if request.method == 'POST':
        # search function
        if 'searchButton' in request.POST:
            formInfo = request.POST.copy()
            searchKeyword = formInfo.get('searchField').strip().replace('  ', ' ')
            if searchKeyword:
                movies = Matabase.objects.filter(Q(title__contains=searchKeyword) | Q(year__exact=searchKeyword))
                # Tags(movies)
                context = {'movies': movies, 'genres': genres, 'count': count, 'footer': footer}
            elif not searchKeyword and not formInfo.get('titleField') and not formInfo.get('yearField'):
                # search not found condition
                movies = []
                context = {'movies': movies, 'genres': genres, 'count': count, 'footer': footer}
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
                movies = Matabase.objects.filter(status='d').order_by('-createdDate', 'title')
            else:
                messages.warning(request, 'New record not save, please provide the movie info completely (both title and year)...')
        elif 'loginButton' in request.POST:
            formInfo = request.POST.copy()
            user = authenticate(username=formInfo.get(
                'username'), password=formInfo.get('password'))
            login(request, user)
            return redirect('homePage')
    context = {'movies': movies, 'genres': genres, 'count': count, 'footer': footer}
    return render(request, 'matabase/home.html', context=context)


def MatabaseUpdate(request, id):
    if request.user.is_authenticated:
        movie = Matabase.objects.filter(id=id).first()
        # tags = Tag(movie)
        if request.method == 'POST':
            formInfo = request.POST.copy()
            movie.title = formInfo.get('titleField')
            movie.year = formInfo.get('yearField')
            movie.status = formInfo.get('statusField')
            movie.save()
            movies = Matabase.objects.filter(id=id)
            context = {'movies': movies, 'genres': genres, 'count': count, 'footer': footer}
            return render(request, 'matabase/home.html', context)
        context = {'movie': movie, 'genres': genres, 'count': count, 'footer': footer}
        return render(request, 'matabase/update.html', context=context)
    else:
        messages.warning(
            request, f'You have no permission to update record, contact your admin for more info.')
    context = {'footer': footer}
    return render(request, 'matabase/home.html', context=context)


def MatabaseDelete(request, id):
    if request.user.is_authenticated:
        try:
            movie = Matabase.objects.filter(id=id).first()
            movie.delete()
            messages.warning(request, f'{movie.title} had been deleted.')
            return redirect('homePage')
        except:
            messages.warning(request, f'Your record id not found.')
            return redirect('homePage')
    else:
        messages.warning(request, f'You have no permission to delete record, contact your admin for more info.')
        return redirect('homePage')


def Dashboard(request):
    # movies = Matabase.objects.all()
    # duplicated = {}
    # for m in movies:
    #     dp = Matabase.objects.filter(Q(title__iexact=m.title) | Q(title__contains=m.title) | Q(year__iexact=m.year))
    #     for d in dp:
    #         duplicated[d.id] = d
    # print(f'DUPLICATED RECORDS: {duplicated}')
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

