from flask import Flask
from .ext import db,csrf,login_manager
# DB MODELS
from .models import *
# BLUEPRINTS
from .mod_main import mod_main_bp
from .mod_users import mod_users_bp
from .mod_owner import mod_owner_bp

def create_app(settings_module):
    app = Flask(__name__,instance_relative_config=True,static_folder='assets')
    app.config.from_object(settings_module)
    # Third party initialization
    db.init_app(app)
    csrf.init_app(app)
    login_manager.init_app(app)
    # Blueprints initialization
    app.register_blueprint(mod_main_bp)
    app.register_blueprint(mod_users_bp)
    app.register_blueprint(mod_owner_bp)
    return app