from flask_wtf import FlaskForm
# from flask_uploads import UploadSet, IMAGES
from wtforms import StringField, PasswordField, FileField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class UploadForm(FlaskForm):
    upload = FileField('image', validators=[FileRequired(),FileAllowed(['jpg', 'png', 'Images only!'])])