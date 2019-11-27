import datetime
from flask import Blueprint

svolgi_bp = Blueprint("svolgi", __name__)

@svolgi_bp.route("/")
def index():
    return "Sono su svolgi"

