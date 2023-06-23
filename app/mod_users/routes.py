from app.ext import db
from flask import Blueprint,request,render_template,redirect,url_for
from flask_login import login_required,login_user,logout_user,current_user
from werkzeug.security import generate_password_hash,check_password_hash
# MODELS
from app.models import Users,Owners,Business
# FORMS
from .forms import LoginForm,SignupForm

mod_users_bp = Blueprint('mod_users_bp', __name__)

@mod_users_bp.route('/signin', methods=['GET','POST'])
def signin():
    form = LoginForm()
    if request.method == 'GET':
        if not current_user.is_authenticated:
            return render_template('signin.html', form=form)
        else:
            return redirect(url_for('mod_owner_bp.profile'))
    elif request.method == 'POST':
        try:
            if not form.validate_on_submit(): raise Exception('Datos no válidos')
            username = form.username.data
            password = form.password.data
            user = Users.query.filter(Users.username == username).first()
            if user is not None and check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('mod_owner_bp.profile'))
            else:
                return redirect(url_for('mod_main_bp.index'))
        except Exception as e:
            return redirect(url_for('mod_users_bp.logout'))


@mod_users_bp.route('/signup', methods=['GET','POST'])
def signup():
    form = SignupForm()
    if request.method == 'GET':
        if not current_user.is_authenticated:
            return render_template('signup.html', form=form)
        else:
            return redirect(url_for('mod_owner_bp.profile'))
    elif request.method == 'POST':
        try:
            if not form.validate_on_submit(): raise Exception('Invalid Form')
            first_name = form.first_name.data
            last_name = form.last_name.data
            email = form.email.data
            username = form.username.data
            password = form.password.data
            new_user = Users()
            new_user.username = username
            new_user.password = generate_password_hash(password)
            db.session.add(new_user)
            db.session.flush()
            new_owner = Owners()
            new_owner.first_name = first_name
            new_owner.last_name = last_name
            new_owner.email = email
            new_owner.user_id = new_user.id
            db.session.add(new_owner)
            db.session.flush()
            new_business = Business()
            new_business.owner_id = new_owner.id
            db.session.add(new_business)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('mod_owner_bp.profile'))
        except Exception as e:
            db.session.rollback()
            return render_template('signup.html', form=form)


@mod_users_bp.route('/logout', methods=['GET'])
@login_required
def logout():
    try:
        logout_user()
    except:
        pass
    finally:
        return redirect(url_for('mod_users_bp.signin'))