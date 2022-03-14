from app import app, db
from flask import render_template, redirect, url_for, flash, get_flashed_messages
from datetime import datetime

from models import Task

import forms

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rapel')
def rapel():
    return render_template('rapel.html')

@app.route('/via-ferrata')
def via():
    return render_template('via_ferrata.html')

@app.route('/escalar')
def escalar():
    return render_template('escalar.html')

@app.route('/camp')
def camp():
    return render_template('camp.html')

@app.route('/registro', methods=['GET','POST'])
def registro():
    form = forms.registration()
    if form.validate_on_submit():
        print('registration complete')
        return redirect(url_for('gracias'))
    return render_template('registro-form.html',form=form)

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/gracias')
def gracias():
    return render_template('gracias.html')
