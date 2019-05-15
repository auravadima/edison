from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    number = StringField('Число для предсказания (Предсказывают до 5)', validators=[DataRequired()])
    submit = SubmitField('Post')
