from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired, Length

class MessageForm(Form):
	title = TextField('Title', validators=[DataRequired()])
	description = TextField('Discription', validators=[DataRequired(), Length(max=140)])

