from flask_wtf import Form
from wtforms import StringField, BooleanField, PasswordField, TextAreaField, SelectField, RadioField, IntegerField
from wtforms.validators import DataRequired

class LoginForm(Form):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember_me = BooleanField('Remember me')

class AddFolderForm(Form):
	folder_name = StringField('Folder Name', validators=[DataRequired()])
	keywords = TextAreaField('Keywords', validators=[DataRequired()])
	# folio_id = StringField('RookMedia Folio ID')

class AddDomainForm(Form):
	domain_name = StringField('Domain Name', validators=[DataRequired()])
	purchase = BooleanField('Purchase Domain', default='checked')
	purchase_privacy = BooleanField('Purchase Privacy', default='checked')
	folder_name = SelectField('Folder Name', coerce=int)
	parker_name = RadioField("Domain Parker's name", validators=[DataRequired()],
		choices = [('pk1', 'Parking Crew (SunDial)'), ('pk2', 'Parking Crew (VolumeDirect)'), ('rm', 'Rook Media')])
	contact = SelectField('Contact Name')

class SelectFolderForm(Form):
	folder_name = SelectField('Folder Name', coerce=int)

class EditCredentialsForm(Form):
	username = StringField('Master Username', validators=[DataRequired()])
	password = StringField('Master Password', validators=[DataRequired()])
	alpnames_reseller_id = IntegerField('AlpNames Reseller ID', validators=[DataRequired()])
	alpnames_api_key = StringField('AlpNames API Key', validators=[DataRequired()])
	alpnames_customer_id = IntegerField('AlpNames Customer ID', validators=[DataRequired()])
	parkingcrew_username_1 = StringField('ParkingCrew Username', validators=[DataRequired()])
	parkingcrew_api_key_1 = StringField('ParkingCrew API Key', validators=[DataRequired()])
	parkingcrew_username_2 = StringField('ParkingCrew Username', validators=[DataRequired()])
	parkingcrew_api_key_2 = StringField('ParkingCrew API Key', validators=[DataRequired()])