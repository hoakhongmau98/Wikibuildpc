from flask import render_template, Blueprint
from .index.process import getdata

main_blueprint = Blueprint('main', __name__)


@main_blueprint.route('/')
def index():
    index_data = getdata()
    return render_template('index.html', index_data=index_data)


@main_blueprint.route('/build')
def build():
    return render_template('build/build.html')

