# views.py

from form import GetRubricResults

def get_semester():


def get_courses(userId): # will need semester code and user id
	my_url = uc.create_authenticated_url(
		'/d2l/api/lp/{0}/enrollments/users/{1}/orgUnits/'.format(VER, userId)) # VER from config, 
	kwargs = {'params': {}}
	kwargs['params'].update({'roleId':ROLE_ID})
	kwargs['params'].update({'orgUnitTypeId': ORG_UNIT_TYPE_ID})
	r = requests.get(my_url, **kwargs)

	# use Kim's code to create dicts for courses offered the same semester for easy retreival

	if request.method == 'POST':
		form = GetRubricResults(request.POST, obj=courses)
		form.courseId.choice = [(i.id, i.name) for i in ???]
		#then we'll redirect to getting dropboxes
	else: #it's request, so display the list of courses


def get_dropboxes(courseId): # will need 
	my_url = uc.create_authenticated_url(
		'/d2l/api/le/{0}/{1}/dropbox/folders/'.format(VER, courseId))
	r = requests.get(my_url, **kwargs)

	if request.method == 'POST':
		form = GetRubricResults(request.POST, obj=courses)
		form.folderId.choice = [(i.id, i.name) for i in ???]
		#then redirect to getting submissions
	else: #it's request, so display the list of dropboxes


def get_submissions(courseId, folderId):
	my_url = uc.create_authenticated_url(
		'/d2l/api/le/{0}/{1}/dropbox/folders/{2}/submissions/'.format(
		VER, courseId, folderId))
	r = requests.get(my_url, **kwargs)
	# returns data--need to process json results
