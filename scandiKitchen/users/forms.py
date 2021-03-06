from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField,FileAllowed
from flask_login import current_user
from scandiKitchen.models import User

#creating input fields for login
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Log In')

#creating input fields for registration
class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    username = StringField('UserName', validators=[DataRequired()])
    #creating password field and linking password to confirm password
    password = PasswordField('Password',validators=[DataRequired(),EqualTo('confirm_password')])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired()])
    submit = SubmitField('Register')

    #check if user provided email and username is already existing
    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('This email already exists')

    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('This username already exists')

#user can update or edit their email and username
class UpdateUserForm(FlaskForm):
     email = StringField('Email', validators=[DataRequired(),Email()])
     username = StringField('UserName', validators=[DataRequired()])
     picture = FileField('Update profile picture',validators=[FileAllowed(['jpg','png'])])
     submit = SubmitField('Update')

     def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('This email already exists')

     def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('This username already exists')


