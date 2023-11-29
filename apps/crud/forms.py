from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, length


class UserForm(FlaskForm):
    username = StringField(
        "username",
        validators=[
            DataRequired(message='username is required'),
            length(max=30, message="username can't be over 30 letters"),
        ],
    )

    email = StringField(
        "email",
        validators=[
            DataRequired(message="email is required"),
            Email(message="please input an email in the email form"),
        ],
    )

    password = PasswordField(
        "password",
        validators=[
            DataRequired(message="password is required"),
        ],
    )

    submit = SubmitField("register")
