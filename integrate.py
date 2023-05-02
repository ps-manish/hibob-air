import requests
import json

# API endpoint URLs
hibob_url = 'https://api.hibob.com/v1/employees'
airtable_url = 'https://api.airtable.com/v0/YOUR_BASE_ID/YOUR_TABLE_NAME'

# API authentication headers
hibob_headers = {'Authorization': 'Bearer YOUR_HIBOB_API_KEY'}
airtable_headers = {
    'Authorization': 'Bearer YOUR_AIRTABLE_API_KEY',
    'Content-Type': 'application/json'
}

# Get employee data from hibob API
response = requests.get(hibob_url, headers=hibob_headers)
employees = response.json()['data']

# Iterate over each employee and update the corresponding Airtable record
for employee in employees:
    # Extract employee data
    name = employee['attributes']['fullName']
    email = employee['attributes']['email']
    # Create Airtable record data
    data = {'fields': {'Name': name, 'Email': email}}
    # Update Airtable record using API
    response = requests.post(airtable_url, headers=airtable_headers, data=json.dumps(data))
    print('Updated record for employee:', name)
