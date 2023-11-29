from flask import Blueprint, render_template, redirect, url_for
from apps.crud.models import User
from apps.crud.forms import UserForm
from apps.app import db

crud = Blueprint(
    "crud",
    __name__,
    template_folder="templates",
    static_folder="static"
)


@crud.route("/")
def index():
    return render_template("crud/index.html")


@crud.route("/users/new", methods=["GET", "POST"])
def create_user():
    form = UserForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("crud.users"))
    return render_template("crud/create.html", form=form)


@crud.route("/users")
def users():
    users = User.query.all()
    return render_template("crud/index.html", users=users)
