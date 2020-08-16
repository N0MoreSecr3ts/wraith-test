#
# secret-key
#
secret-key = "john"
customer-key := "john"
consumer-key := "john"

secret_key = "john"
customer_key := "john"
consumer_key := "john"

secret-key = 'john'
customer-key := 'john'
consumer-key := 'john'

secret_key = 'john'
customer_key := 'john'
consumer_key := 'john'

pwd = "john"
pwd = 'john'

password = "john"
nexuspassword = "john"
pass = "john"

password = 'john'
nexuspassword = 'john'
pass = 'john'

passwd = "john"
passwd = 'john'

cred = "john"
creds = "john"
credentials = "john"
credential = "john"

cred = 'john'
creds = 'john'
credentials = 'john'
credential = 'john'

AUTH_DICT = {'a_key': 'AKIAIGTOPSI4SXYCHGHQ'}

def check_access(key):
    # Comparison with a high entropy string
    if key == 'AKIAIGTOPSI4SXYCHGHQ':
        return True
    # List with high entropy strings
    elif password in ['AKIAIGTOPSI4SXYCHGHQ', 'pmHFdYrNYvOVQWqYjDgL']:
        return True
    return False

# Function definition with a shady looking kwarg and a high
# entropy value.
def call_api(api_key='AKIAIGTOPSI4SXYCHGHQ'):
    expiration = api.call(api_key,'AKIAIGTOPSI4SXYCHGHQ')

access_key = "AKIAIGTOPSI4SXYCHGHQ"
access_key = 'AKIAIGTOPSI4SXYCHGHQ'

auth = "john"
authorization = "john"

auth = 'john'
authorization = 'john'