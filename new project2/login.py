from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Length

class login(FlaskForm):
    Name=StringField(" Username",validators=[DataRequired()])
    Password=PasswordField("Password",validators=[DataRequired(),Length(min=7)])
    Submit=SubmitField("Submit")