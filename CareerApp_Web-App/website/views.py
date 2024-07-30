from flask import Blueprint, render_template, Flask
from flask_login import login_required, current_user
import os
from . import create_app

views = Blueprint('views', __name__)
app = Flask(__name__)

picFolder = os.path.join('static', 'pics')
app.config['UPLOAD_FOLDER'] = picFolder

@views.route('', methods=['GET', 'POST'])
@login_required
def home():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'], 'Jobs.svg')
    return render_template("home.html", user = current_user, user_image = pic1)
    