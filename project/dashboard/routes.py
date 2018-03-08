from flask import render_template

from . import dashboard_blueprint


@dashboard_blueprint.route('/')
def index():
    return render_template('dashboard/dashboard.html')
