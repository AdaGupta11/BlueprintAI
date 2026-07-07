import requests
from config import ORCHESTRATE_IAM_APIKEY

url = "https://iam.cloud.ibm.com/identity/token"

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

data = {
    "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
    "apikey": ORCHESTRATE_IAM_APIKEY
}

response = requests.post(url, headers=headers, data=data)

print("Status Code:", response.status_code)
print(response.json())