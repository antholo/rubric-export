# form.py

from flask_wtf import Form
from wtforms import RadioField, BooleanField


class GetRubricResults(Form):
	courseId = RadioField('Select course', validators=[DataRequired()]) # RadioField(default field arguments, choices=[], coerce=unicode)
	dropboxId = RadioField('Select dropbox', validators=[(DataRequired()])
	feedback = BooleanField('Include feedback?')
