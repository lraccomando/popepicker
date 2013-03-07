from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from popepicker.models import Pope

popes = Blueprint('popes', __name__, template_folder='templates')


class ListView(MethodView):

    def get(self):
        popes = Pope.objects.all()
        return render_template('popes/list.html', popes=popes)


popes.add_url_rule('/', view_func=ListView.as_view('list'))
