from flask_wtf import FlaskForm
from flask_wtf.file import FileField , FileAllowed
from flask_login import current_user
from wtforms import StringField , PasswordField , SubmitField ,BooleanField ,TextAreaField 
from wtforms.validators import DataRequired , length , Email ,EqualTo,ValidationError
from frist.models import User
class RegistrationForm(FlaskForm):
    username=StringField('username',
                         validators=[DataRequired(),length(min=2,max=20)])
    email=StringField('Email',
                      validators=[DataRequired(),Email()])
    password= PasswordField('password',validators=[DataRequired()])
    password_confirm= PasswordField('password confirm',validators=[EqualTo('password')])
    submit= SubmitField('Sign Up')

    def validateusername(self,username):
        user=User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That was taken msh zayk , choose another one.')
            

    def validateemai(self,email):
        user=User.query.filter_by(username=email.data).first()
        if user:
            raise ValidationError('That was taken msh zayk , choose another one.')


class LoginForm(FlaskForm):
    email=StringField('Email',
                      validators=[DataRequired(),Email()])
    password= PasswordField('password',validators=[DataRequired()])
    remember= BooleanField("Remember Me")
    submit= SubmitField('LogIn')


class UpdateAccountForm(FlaskForm):
    username=StringField('username',
                         validators=[DataRequired(),length(min=2,max=20)])
    email=StringField('Email',
                      validators=[DataRequired(),Email()])
    picture=FileField('Update  Profile pic',validators=[FileAllowed(['jpg','png'])])
    submit= SubmitField('Update')

    def validateusername(self,username):
        if username.data != current_user.username:

            user=User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That was taken msh zayk , choose another one.')

    def validateemai(self,email):
        if email.data != current_user.email:

            user=User.query.filter_by(username=email.data).first()
            if user:
                raise ValidationError('That was taken msh zayk , choose another one.')



class PostForm(FlaskForm):
    title=StringField('Title',validators=[DataRequired()])
    content=TextAreaField('Content',validators=[DataRequired()])
    submit=SubmitField('Post')



class ReqResetForm(FlaskForm):
    email=StringField('Email',
                      validators=[DataRequired(),Email()])
    submit=SubmitField('Request Password Reset')
    
    
    
    def validateemai(self,email):
        if email.data != current_user.email:

            user=User.query.filter_by(username=email.data).first()
            if user is None:
                raise ValidationError('there is no account with this email,you must register first..')
            
class ResetPasswordForm(FlaskForm):
    password= PasswordField('password',validators=[DataRequired()])
    password_confirm= PasswordField('password confirm',validators=[EqualTo('password')])
    submit= SubmitField('Confirm')
