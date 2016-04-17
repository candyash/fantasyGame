from flask import render_template, flash, redirect, \
    url_for, abort, request, current_app
from flask.ext.login import login_required, current_user
from ..import db
from ..models import User, PersonalInfo
from . import fast
from .forms import ProfileForm, RegisterForm
from config import Config
from flask.ext.sqlalchemy import Pagination
import sqlalchemy



@fast.route("/", defaults={"page": 1})
@fast.route("/")
def index():
    form = RegisterForm()

    return render_template ("fast/index.html", form=form)
@fast.route("/user/<username>")
def user(username):
    """initializing presonalinfo for the current user"""
    user = User.query.get(current_user.id)
    personal = PersonalInfo.query.\
        filter(PersonalInfo.user_id == current_user.id).first()
    if personal is None:
        #userinfo = PersonalInfo(first_name='***', last_name='***')
        #db.session.add(userinfo)
        #db.session.commit()
        #flash("Please update your profile")
        return redirect(url_for("fast.profile"))
    return render_template('fast/user.html', user=user, personal=personal)

@fast.route("/Register", methods=["GET", "POST"])
def Register():
    """Register a new user."""
    form = RegisterForm()
    try:
        if request.method == "POST" and form.validate_on_submit():
            firstname=form.firstName.data
            lastname=form.lastName.data
            country=form.country.data
            city=form.city.data
            phonenumber=form.phoneNumber.data
            info=PersonalInfo(first_name=firstname, last_name=lastname, country=country, city=city, phonenumber=phonenumber)
            db.session.add(info)
            email = form.email.data
            username = form.username.data
            password = form.password.data
            user = User\
            (email=email, username=username, is_admin=False, password=password)
            db.session.add(user)
            db.session.commit()
            flash("User {0} was registered successfully.".format(username))
            return redirect(url_for("auth.login"))
    except :
        flash("User already exists. Try agin!")


    return render_template("fast/Register.html", form=form)
@fast.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = ProfileForm()
    if form.validate_on_submit():
        current_user.user_info.first_name = form.firstName.data
        current_user.user_info.last_name = form.lastName.data
        current_user.user_info.age = form.Age.data
        current_user.user_info.location = form.location.data
        current_user.user_info.bio = form.bio.data
        current_user.user_info.user_id = current_user.id
        db.session.add(current_user.user_info)
        db.session.commit()
        flash("You have been updated your profile")
        return redirect(url_for('fast.user', username=current_user.username))
    if current_user.user_info:
        form.firstName.data = current_user.user_info.first_name
        form.lastName.data = current_user.user_info.last_name
        form.location.data = current_user.user_info.location
        form.Age.data = current_user.user_info.age
        form.bio.data = current_user.user_info.bio
    return render_template('fast/profile.html', form=form)

@fast.route('/team')
def team():
    return render_template('fast/team.html')

@fast.route('/league')
def  league():
    return render_template('fast/league.html')

@fast.route('/results')
def results():
    return render_template('fast/results.html')
@fast.route('/forum')
def forum():
    return render_template('fast/forum.html')