from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Optional, URL, Regexp


class URLForm(FlaskForm):
    original_link = URLField(
        label='Введите ссылку',
        validators=(
            DataRequired(message='Обязательное поле'),
            URL(message='Некорректный URL')
        )
    )
    custom_id = StringField(
        label='Ваш вариант короткой ссылки',
        validators=(
            Optional(),
            Regexp(r'^[a-zA-Z0-9]{1,16}$',
                   message='Допускается только латиница и арабские цифры. '
                           'Максимальная длина ссылки: 16 символов')
        )
    )
    submit = SubmitField('Создать')

