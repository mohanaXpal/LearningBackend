from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,IntegerField,SelectField
from wtforms.validators import Email,DataRequired,Length,NumberRange

class form(FlaskForm):
    Name=StringField("Full Name",validators=[DataRequired()])
    Age=IntegerField("Age",validators=[DataRequired(),NumberRange(min=10,max=100)])
    Course=SelectField("Course",validators=[DataRequired()],choices=[("CSE","CSE"),("IT","IT"),("DS","DS"),("AiMl","AiMl")])
    Email=StringField("Email",validators=[DataRequired(),Email()])
    Submit=SubmitField("Register")   