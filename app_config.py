
# This configuration file represents the kind of state information that your
# app should store in a separate, more secure, location away from your web-app
# source. This holds especially true for the App ID/Key pair -- this is
# sensitive information, and you should find a way to keep it under tight
# control, restricting access only to those who need to manage the values (system
# administrators, for example).
#
# Here, we just put the config values into a sample dictionary that the web
# framework in basic.py can import.
#
#   app_id --  App ID as provided by D2L -- DON'T HARDCODE INTO YOUR APP
#   app_key -- App Key as provided by D2L -- DON'T HARDCODE INTO YOUR APP
#   host   --  host for the web-app
#   port   --  port number for the web-app
#   scheme --  protocol to use for user <--> web-app interaction
#   lms_host -- hostname for the back-end LMS
#   lms_port -- port number for the back-end LMS
#   encrypt_requests -- True: use HTTPS when making API calls to the LMS
#   lms_ver -- product component API versions to call
#   verify -- cert verification flag
#   debug -- debug flag

APP_ID = 'PkThAwhB0a3Xg6R2SjVugg'
APP_KEY = 'hrzc1K0SZ_Co1T5jV26EAw'
HOST = 'localhost'
PORT = '5000'
SCHEME = 'HTTP'
LMS_HOST = 'uwosh-beta.courses.wisconsin.edu'
LMS_PORT = '443'
ENCRYPT_REQUESTS = True
VERIFY = False
LMS_VER = {'lp':1.3,'le':10.3,'ep':2.3}
# API version
VER = '1.4'

# authorization route
AUTH_ROUTE = "/token"

# authorization callback route
AUTH_CB = '{0}://{1}:{2}{3}'.format(SCHEME, HOST, PORT, AUTH_ROUTE)

# constants for API calls
# code for course in orgunits APi route call
ORG_UNIT_TYPE_ID = '3'

# code of instructor role in orgunits call
ROLE_ID = '914'

# service account ID and Key
USER_ID = 'pH691N4IkwTRUYspzQKaF_'
USER_KEY = 'qBKaRduHxQxmiE1Q5gkN3y'


DEBUG = True
