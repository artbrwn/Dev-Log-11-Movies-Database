from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class CommentsForm(FlaskForm):
    user_name = StringField("user_name", validators=[DataRequired("El campo nombre no puede estar vacío."), Length(min=2, message="El campo nombre debe contener al menos 2 caracteres.")])
    comment = TextAreaField("comment",  validators=[DataRequired("El campo comentario no puede estar vacío."), Length(min=2, message="El campo comentario debe contener al menos 2 caracteres.")])

    save = SubmitField("save")