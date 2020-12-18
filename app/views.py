from flask import render_template, Blueprint
from .index.process import getdata
from .compoments.getlistimg import getimg

main_blueprint = Blueprint('main', __name__)


@main_blueprint.route('/')
def index():
    index_data = getdata()
    return render_template('index.html', index_data=index_data)


@main_blueprint.route('/build')
def build():
    return render_template('build/build.html')


@main_blueprint.route('/Main')
def mainboard():
    index_object = getimg('Main')
    return render_template('components/Main.html', index_object=index_object)


@main_blueprint.route('/Ram')
def ram():
    index_object = getimg('Ram')
    return render_template('components/Ram.html', index_object=index_object)
