# form.py

from flask_wtf import Form
from wtforms import RadioField, BooleanField, SelectField
from datetime import date

# semester values for four-digit semester codes
FALL = '0'
SPRING = '5'
SUMMER = '8'

# base year for calculating semester code
BASE_YEAR = 1945


class GetRubricResults(Form):
	semester = SelectField('Select semester', choices=[(FALL, 'Fall'), (SPRING, 'Spring'), (SUMMER, 'Summer')])
	year = SelectField('Select year', choices=[(str(year - BASE_YEAR), str(year)) for year in range(date.today().year - 6, date.today().year)]
	courseId = RadioField('Select course', validators=[DataRequired()]) # RadioField(default field arguments, choices=[], coerce=unicode)
	dropboxId = RadioField('Select dropbox', validators=[(DataRequired()])
	feedback = BooleanField('Include feedback?')
