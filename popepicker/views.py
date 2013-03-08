from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from flask.ext.jsonify import jsonify
from popepicker.models import Pope


popes = Blueprint('popes', __name__, template_folder='templates')


class HomeView(MethodView):

    def get(self):
        return render_template('popes/index.html')


class PopeView(MethodView):

    @jsonify
    def get(self):
        popes = Pope.objects.all()
        return dict(popes=popes)


popes.add_url_rule('/', view_func=HomeView.as_view('home'))
popes.add_url_rule('/data/popes/', view_func=PopeView.as_view('popes'))
