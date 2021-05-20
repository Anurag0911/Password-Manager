from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Password
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        site = request.form.get('site')
        username = request.form.get('username')
        password = request.form.get('password')
        note = request.form.get('note')

        if len(password) < 1:
            flash('Password is too short!', category='error')
        else:
            new_Password = Password(site=site, username=username, password=password,data=note, user_id=current_user.id)
            db.session.add(new_Password)
            db.session.commit()
            flash('Added!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-password', methods=['POST'])
def delete_password():
    password = json.loads(request.data)
    passwordId = password['passwordId']
    password = Password.query.get(passwordId)
    if password and password.user_id == current_user.id:
        db.session.delete(password)
        db.session.commit()

    return jsonify({})
