# views.py

from flask import Flask, flash, redirect, render_template, request, session, url_for
from form import GetRubricResults
from functools import wraps
import requests
import os
import auth2 as d2lauth

app = Flask(__name__)
app.config.from_pyfile('app_config.py')

appContext = d2lauth.fashion_app_context(app_id=app.config['APP_ID'],
                                         app_key=app.config['APP_KEY'])


@app.route('/')
@app.route('/login')
def login():
    '''
    Checks if user context is stored in session and redirects to authorization handler if it is.
    If not, renders login template with link to D2L login and callback route to authorization handler.
    '''
    if 'userContext' in session:
        return redirect(url_for('auth_handler'))
    else:
        authUrl = appContext.create_url_for_authentication(
            host=app.config['LMS_HOST'],
            client_app_url=app.config['AUTH_CB'],
            encrypt_request=app.config'[ENCRYPT_REQUESTS'])
        print(authUrl)
        return render_template('login.html', authUrl=authUrl)


@app.route(app_config.AUTH_ROUTE)
def auth_handler():
    '''
    Authorizes logged in user. Stores authorized user info via call to API 
    whoami route. Then authorizes service account. 
    '''
    print("Request uri", request.url)
    uc = appContext.create_user_context(
        result_uri=request.url, 
        host=app.config['LMS_HOST'],
        encrypt_requests=app.config['ENCRYPT_REQUESTS'])
    print("User Context", uc)
    # call whoami and store user info
    my_url = uc.create_authenticated_url('/d2l/api/lp/{0}/enrollments/myenrollments'.format(app.config['VER']))
    r = requests.get(my_url, **kwargs)
    session['firstName'] = r.json()['FirstName']
    session['lastName'] = r.json()['LastName']
    session['userId'] = r.json()['Identifier']

    # feed in service account ID and key and store user context
    uc.user_id = app.config['USER_ID']
    uc.user_key = app.config['USER_KEY']
    session['userContext'] = uc.get_context_properties()
    #
    #
    #
    # Need route for form
    return redirect(url_for(???))


@app.route(???) # need form route here, too
def get_results():
    '''
    This function will drive the form.
    Will call functions to get more information as user makes selections in the form. 
    This page gives info on how to do this:
    http://wtforms.simplecodes.com/docs/1.0.3/fields.html#wtforms.fields.SelectField
    First, a call will be made using the get_courseList route to create a course dictionary keyed by semester code
    Users will select semester and year and get_semester will be called to generate the semester code
    This info will be used to pull the course IDs and names from courseList
    This same info will populate the radiofields
    User will select the course, and the courseID will be passed to a function to get dropboxes...

    '''
	error = None
	form = GetRubricResults(request.form)
	if request.method == 'POST':
		if form.validate_on_submit():
    if request.method == 'POST':
        form = GetRubricResults(request.POST, obj=courses)
        form.courseId.choices = [(courseId, courseName) for courseId, courseName in courseList['courseId'], courseList['name']]
        #then we'll redirect to getting dropboxes
    else: #it's request, so display the list of courses

def get_semester(semester, year):
	if semester == 'Fall':
        precedingDigits = year
        finalDigit = '0'
    if semester == 'Spring':
        precedingDigits = str(int(year) - 1)
        finalDigit = '5'
    if semester == 'Summer':
        precedingDigits = str(int(year) - 1)
        finalDigit = '8'
    semesterCode = precedingDigits + finalDigit
    if len(semesterCode) < 4:
        semesterCode = '0' + semesterCode
    return(semesterCode)



def get_courseList(): # will need semester code and user id
	myUrl = uc.create_authenticated_url(
		'/d2l/api/lp/{0}/enrollments/users/{1}/orgUnits/'.format(app.config['VER'], uc.user_id)) # VER from config, 
	kwargs = {'params': {}}
	kwargs['params'].update({'roleId':app.config['ROLE_ID']})
	kwargs['params'].update({'orgUnitTypeId': app.config['ORG_UNIT_TYPE_ID']})
	r = requests.get(my_url, **kwargs)
    courseList = {}
    end = False
    while end == False:
        for course in r.json()['Items']:
            semCode = str(course['OrgUnit']['Code'][6:10])
            if semCode.isdigit():
                if semCode not in courseList:
                    courseList[semCode] = []
                courseList[semCode].append({'courseId': course['OrgUnit']['Code'], 'name': course['OrgUnit']['Name']})
            if r.json()['PagingInfo']['HasMoreItems'] == True:
                kwargs['params']['bookmark'] = r.json()['PagingInfo']['Bookmark']
                r = requests.get(my_url, **kwargs)
        else:
            end = True
    return(courseList)







def get_dropboxes(courseId): # will need 
	myUrl = uc.create_authenticated_url(
		'/d2l/api/le/{0}/{1}/dropbox/folders/'.format(app.config['VER'], courseId))
	r = requests.get(my_url, **kwargs)

	if request.method == 'POST':
		form = GetRubricResults(request.POST, obj=courses)
		form.folderId.choices = [(i.id, i.name) for i in ???]
		#then redirect to getting submissions
	else: #it's request, so display the list of dropboxes


def get_submissions(courseId, folderId):
	my_url = uc.create_authenticated_url(
		'/d2l/api/le/{0}/{1}/dropbox/folders/{2}/submissions/'.format(
		app.config['VER'], courseId, folderId))
	r = requests.get(my_url, **kwargs)
	# returns data--need to process json results


app.secret_key = os.urandom(24)


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])