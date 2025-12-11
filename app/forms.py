from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=3, max=80)])
    password = PasswordField("Password", validators=[DataRequired()])

class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=3, max=80)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=4)])
    role = SelectField("Role", choices=[("Tester", "Tester"), ("Developer", "Developer"), ("Admin", "Admin")])

class TicketForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(max=140)])
    description = TextAreaField("Description")
    priority = SelectField("Priority", choices=[("Low", "Low"), ("Medium", "Medium"), ("High", "High"), ("Critical", "Critical")])
    assignee = SelectField("Assign to", choices=[], coerce=int, default=0)
    submit = SubmitField("Submit")
