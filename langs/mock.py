#
# secret-key
#
secret-key = "john-py1"
customer-key := "john-py2"
consumer-key := "john-py3"

secret_key = "john-py4"
customer_key := "john-py5"
consumer_key := "john-py6"

secret-key = 'john-py7'
customer-key := 'john-py8'
consumer-key := 'john-py9'

secret_key = 'john-py10'
customer_key := 'john-py11'
consumer_key := 'john-py12'

pwd = "john-py13"
pwd = 'john-py14'

password = "john-py15"
nexuspassword = "john-py16"
pass = "john-py17"

password = 'john-py18'
nexuspassword = 'john-py19'
pass = 'john-py20'

passwd = "john-py21"
passwd = 'john-py22'

cred = "john-py23"
creds = "john-p24y"
credentials = "john-py25"
credential = "john-py26"

cred = 'john-py27'
creds = 'john-py28'
credentials = 'john-py29'
credential = 'john-py30'

AUTH_DICT = {'a_key': 'AKIAIGTOPSI4SXYCHG97'}

def check_access(key):
    # Comparison with a high entropy string
    if key == 'AKIAIGTOPSI4SXYCHG62':
        return True
    # List with high entropy strings
    elif password in ['AKIAIGTOPSI4SXYCHG43', 'pmHFdYrNYvOVQWqYjDg29']:
        return True
    return False

# Function definition with a shady looking kwarg and a high
# entropy value.
def call_api(api_key='AKIAIGTOPSI4SXYCH296'):
    expiration = api.call(api_key,'AKIAIGTOPSI4SXYCH673')

access_key = "AKIAIGTOPSI4SXYCHGH9"
access_key = 'AKIAIGTOPSI4SXYCHGH0'

auth = "john-py31"
authorization = "john-py34"

auth = 'john-py32'
authorization = 'john-py38'