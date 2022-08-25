# lovie
Movie database develop with multiple web frameworks

## branch
`git clone --branch <branchName> --single-branch https://github.com/lanuxos/lovie.git`
### django
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
- Add record(s) [only staff permission]
- Search records
- List records via status [all, watched, downloaded, deleted]

## Future features
- Registered could edit tag(s), add pending record(s) and approve via staff