from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, TextAreaField, SelectField, SelectMultipleField, RadioField
from wtforms.validators import DataRequired, Length

from .models import User

from flask_babel import gettext


class LoginForm(FlaskForm):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


class EditForm(FlaskForm):
    nickname = StringField('nickname', validators=[DataRequired()])
    about_me = TextAreaField('about_me', validators=[Length(min=0, max=140)])

    def __init__(self, original_nickname, *args, **kwargs):
        FlaskForm.__init__(self, *args, **kwargs)
        self.original_nickname = original_nickname

    def validate(self):
        if not FlaskForm.validate(self):
            return False
        if self.nickname.data == self.original_nickname:
            return True
        if self.nickname.data != User.make_valid_nickname(self.nickname.data):
            self.nickname.errors.append(gettext(
                'This nickname has invalid characters. Please use letters, numbers, dots and underscores only.'))
            return False
        user = User.query.filter_by(nickname=self.nickname.data).first()
        if user is not None:
            self.nickname.errors.append('This nickname is already in use. Please choose another one.')
            return False
        return True


class PostForm(FlaskForm):
    post = StringField('post', validators=[DataRequired()])


class SearchForm(FlaskForm):
    search = StringField('search', validators=[DataRequired()])


class TestForm(FlaskForm):
    string_field = StringField('openid', validators=[DataRequired()], default='язх234')
    boolean_field = BooleanField('BooleanField', default=True)
    text_area_field = TextAreaField('TextAreaField', validators=[Length(min=0, max=140)], default='хзфыв34')
    select_field = SelectField('SelectField')
    select_multiple_field = SelectMultipleField('SelectMultipleField')
    radio_field = RadioField('RadioField')

    def __init__(self, *args, **kwargs):
        FlaskForm.__init__(self, *args, **kwargs)

        choices = [('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')]
        self.select_field.choices = choices
        self.select_multiple_field.choices = choices
        self.radio_field.choices = choices
