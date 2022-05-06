from flask import render_template, flash, abort, redirect

from . import app, db
from .forms import URLForm
from .models import URL_map
from .utils import check_short_url, get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLForm()
    if form.validate_on_submit():
        original = form.original_link.data
        short = form.custom_id.data
        if short:
            if check_short_url(short):
                flash(f'Имя занято {short} уже занято!')
                return render_template('main_page.html', form=form)
        if short is None:
            short = get_unique_short_id()
        url_link = URL_map(
                original=original,
                short=short
            )
        db.session.add(url_link)
        db.session.commit()
        flash('Ваша новая ссылка готова:')
        flash(short)
    return render_template('main_page.html', form=form)


@app.route('/<string:short_url>')
def redirect_to_url(short_url):
    original_url = URL_map.query.filter_by(short=short_url).first()
    if original_url is None:
        abort(404)
    return redirect(original_url.original)
