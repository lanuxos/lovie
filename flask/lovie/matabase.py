from flask import (Blueprint, flash, g, redirect, render_template, request, url_for)
from werkzeug.exceptions import abort
from lovie.auth import login_required
from lovie.db import get_db

bp = Blueprint('matabase', __name__)

@bp.route('/')
def home():
    db = get_db()
    movies = db.execute(
        'SELECT m.id, title, year, status, user, createdDate, updatedDate, u.username'
        ' FROM matabase m JOIN user u ON m.user = u.id'
        ' ORDER BY createdDate DESC'
    ).fetchall()
    return render_template('matabase/home.html', movies = movies)

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        year = request.form['year']
        status = request.form['status']
        error = None

        if not title:
            error = 'Title is required.'
        if not status:
            status = 'downloaded'
        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO matabase (title, year, status, user)'
                ' VALUES (?, ?, ?, ?)',
                (title, year, status, g.user['id'])
            )
            db.commit()
            return redirect(url_for('matabase.home'))
    return render_template('matabase/create.html')


def get_movie(id, check_author=True):
    movie = get_db().execute(
        'SELECT m.id, title, year, status, createdDate, user'
        ' FROM matabase m JOIN user u ON m.user = u.id'
        ' WHERE m.id = ?',
        (id,)
    ).fetchone()

    if movie is None:
        abort(404, f"Movie id {id} doesn't exist.")

    if check_author and movie['user'] != g.user['id']:
        abort(403)

    return movie


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    movie = get_movie(id)

    if request.method == 'POST':
        title = request.form['title']
        year = request.form['year']
        status = request.form['status']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE matabase SET title = ?, year = ?, status = ?'
                ' WHERE id = ?',
                (title, year, status, id)
            )
            db.commit()
            return redirect(url_for('matabase.home'))

    return render_template('matabase/update.html', movie=movie)


@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_movie(id)
    db = get_db()
    db.execute('DELETE FROM matabase WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('matabase.home'))


