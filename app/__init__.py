from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.settings.config import SQLALCHEMY_DATABASE_URI


# from controllers.creaController import crea_bp
# from controllers.homeController import home_bp
# from controllers.svolgiController import svolgi_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)



#app.register_blueprint(crea_bp, url_prefix="/crea")
#app.register_blueprint(svolgi_bp, url_prefix="/svogli")
#app.register_blueprint(home_bp, url_prefix="/")


