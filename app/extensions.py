from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_talisman import Talisman
from flask_wtf import CSRFProtect

db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()
talisman = Talisman()

login_manager.login_view = "auth.login"
login_manager.login_message_category = "warning"
