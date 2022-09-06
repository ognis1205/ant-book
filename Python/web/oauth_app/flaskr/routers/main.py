from flask import Blueprint, render_template
from flask_login import login_required, current_user


bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template('main/index.html')


#@bp.route('/profile')
#@login_required
#def profile():
#    return render_template('main/profile.html', name=current_user.name)
