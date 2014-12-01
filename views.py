# views.py

from form import GetRubricResults

def get_courses(userId): # will need semester code and user id
	my_url = uc.create_authenticated_url('/d2l/api/lp/{0}/enrollments/users/{1}/orgUnits/'.format(VER, userId)) # VER from config, 
	kwargs = {'params': {}}
	kwargs['params'].update({'roleId':ROLE_ID})
	kwargs['params'].update({'orgUnitTypeId': ORG_UNIT_TYPE_ID})
	r = requests.get(my_url, **kwargs)

	if request.method == 'POST':
		form = GetRubricResults(request.POST, obj=courses)
		form.courseId.choice = [(i.id, i.name) for i in ]
		#then we'll redirect to getting dropboxes
	else: #it's request, so display the list of courses


def get_dropboxes(???):
	form = GetRubricResults(request.form)
	if request.method == 'POST':
