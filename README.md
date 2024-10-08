# lovie
Movie database develop with multiple web frameworks

## branch
```
git clone --branch <branchName> --single-branch https://github.com/lanuxos/lovie.git
git push --set-upstream origin <branchName>
```
### django
- django
- bootstrap
- djangorestframework
- commented out urls.py models.py admin.py views.py before migrate database, preventing model error
```
git checkout -b django
python -m virtualenv venv
.\venv\Script\activate  # for Windows user, use source ./venv/bin/activate instead for mac user
python -m pip install django
python manage.py migrate
python manage.py createsuperuser
python manage.py loaddata footer.json  # to load data from fixtures file named Footer
python manage.py loaddata db.json  # to load data from fixtures file named db
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
- Pagination

## bugs
- links/developer info divide, fetch whole and count then divide by 2 ?
- project initialization error, footer models migration error, footer fixtures

## Future features
- Registered could edit tag(s), add pending record(s) and approve via staff
- plot history statistic graph, store user's changing record [watched/deleted] then count as activity
- scrapping tag info from mdb, set untag if there is no found info
- remove [pop()] UNTAG if the len() > 1
- dataTable on search result for sorting via name/tags/year
- scrape genes tag from imdb while adding new record, add update btn to fetch on update page
- API