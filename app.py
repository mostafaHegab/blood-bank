from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

from db.init import conn, create_tables
from utils.config import DB_CONFIG

# blueprints imports
from blueprints.auth_blueprint import auth
from blueprints.system_admin_blueprint import sys_admin
from blueprints.user_blueprint import user
from blueprints.blood_bank_blueprint import bank
from blueprints.hospital_blueprint import hospital
from blueprints.api_blueprint import api


app = Flask(__name__, template_folder='views', static_folder='assets')

app.config['SQLALCHEMY_DATABASE_URI'] = DB_CONFIG['databaseURL']
db = SQLAlchemy(app)
SESSION_TYPE = "sqlalchemy"
SESSION_SQLALCHEMY = db
SESSION_SQLALCHEMY_TABLE = "sessions"
app.config.from_object(__name__)
sess = Session(app)
sess.app.session_interface.db.create_all()

# blueprint registers
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(sys_admin, url_prefix='/sys-admin')
app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(bank, url_prefix='/bank')
app.register_blueprint(hospital, url_prefix='/hospital')
app.register_blueprint(api, url_prefix='/api')

if __name__ == "__main__":
    c = conn.cursor()
    c.execute('''SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' ORDER BY table_name''')
    res = c.fetchall()
    c.close()
    if len(res) == 0 or len(res) == 1:
        create_tables()
    app.run(port=5000, threaded=True, debug=True)
