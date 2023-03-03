from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
#necessary tools for web validation
# always install email_validator, flask-wtf, wtforms, generate secret_key by import os on terminal followed by os.
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User
# for user authentication, do pip install flask_bcrypt in the terminal. this would help generate hash password

class RegisterForm(FlaskForm): 
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user: # This means if username already exist in the database
            raise ValidationError('Username already exists! Please try anothe username')
    
    def validate_email_address(self, email_address_to_check):
        user = User.query.filter_by(email_address=email_address_to_check.data).first()
        if user:
            raise ValidationError('Email Address alraedy exist! Please try another Email Address')
            
    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit=SubmitField(label='Create Account')
    
class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit=SubmitField(label='Sign in')
    
class PurchaseItemForm(FlaskForm):
    submit=SubmitField(label='Purcase Item')
    
class SellItemForm(FlaskForm):
    submit=SubmitField(label='Sell Item')