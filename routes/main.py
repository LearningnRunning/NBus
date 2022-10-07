from flask import Blueprint, render_template

bp = Blueprint('main', __name__, url_prefix='/main')

@bp.route('/')
def main():
    return render_template('index.html')