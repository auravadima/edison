from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange


class PostForm(FlaskForm):
    number = IntegerField('Число для предсказания (Предсказывают до 5)',
                          validators=[DataRequired(), NumberRange(min=0, max=5)])
    submit = SubmitField('Post')
