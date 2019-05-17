from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange


class PostForm(FlaskForm):
    number = IntegerField('Загаданное число',
                          validators=[DataRequired(), NumberRange(min=0, max=99)])
    submit = SubmitField('Отправить число')

class ReadyForm(FlaskForm):
    submit = SubmitField('Загадал, хочу получить предположения экстрасенсов')