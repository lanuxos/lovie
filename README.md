# lovie
Movie database develop with multiple web frameworks

## branch
```
git clone --branch <branchName> --single-branch https://github.com/lanuxos/lovie.git
git push --set-upstream origin <branchName>
```
### django
- django 4.1
- bootstrap 5.2
```
git checkout -b django
python -m virtualenv venv
.\venv\Script\activate  # for Windows user, use source ./venv/bin/activate instead for mac user
python -m pip install django==4.1
python manage.py migrate
python manage.py createsuperuser
python manage.py loaddata fixtures/Footer  # to load data from fixtures file named Footer
python manage.py runserver
# visit localhost:8000/matabase/home or localhost:8000/admin
```
### fastApi
### flask
```
git checkout -b flask

py -m venv venv
.\venv\Script\activate
pip install Flask

# flask --app <APP_NAME> --debug run
flask --app lovie --debug run

```
#### project layout
- lovie/
    - __init__.py
    - auth.py
    - db.py
    - matabase.py
    - schema.sql
    - static/
        - style.css
    - templates/
        - auth/
            - login.html
            - register.html
        - base.html
        - matabase/
            - create.html
            - home.html
            - update.html
- MANIFEST.in
- setup.py
- tests/
    - conftest.py
    - data.sql
    - test_auth.py
    - test_db.py
    - test_factory.py
    - test_matabase.py
- venv/

### laravel

## Features
- User system
- Add, update/edit or delete record(s) [only staff permission]
- Search records
- List records via status [all, watched, downloaded, deleted]

## bugs
- links/developer info divide, fetch whole and count then divide by 2 ?

## Future features
- Registered could edit tag(s), add pending record(s) and approve via staff
- plot history statistic graph, store user's changing record [watched/deleted] then count as activity
- scrapping tag info from mdb, set untag if there is no found info
- remove [pop()] UNTAG if the len() > 1
- dataTable on search result for sorting via name/tags/year
- scrape genes tag from imdb while adding new record, add update btn to fetch on update page