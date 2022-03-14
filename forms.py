from flask_wtf  import FlaskForm
from wtforms import StringField, DateField, IntegerField, SelectField, EmailField, TelField, SubmitField
from wtforms.validators import DataRequired

class registration(FlaskForm):

    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    id_type = SelectField('Type of ID', choices=['CC', 'Pasaporte'], validators=[DataRequired()])
    id_number = IntegerField('Type of ID', validators = [DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    phone = TelField('Telephone', validators=[DataRequired()])
    e_phone = TelField('Emergency Telephone', validators=[DataRequired()])

    activity = SelectField('Activity',choices=['Rapel', 'Via Ferrata','Escalar','Camp'], validators=[DataRequired()])
    date_activity = DateField('Date of Activity', validators=[DataRequired()])
    submit = SubmitField('Submit')
