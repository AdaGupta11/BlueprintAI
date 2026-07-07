import requests
from config import ORCHESTRATE_IAM_APIKEY, ORCHESTRATE_URL

# Step 1: Get IAM Access Token
iam_url = "https://iam.cloud.ibm.com/identity/token"

iam_response = requests.post(
    iam_url,
    headers={
        "Content-Type": "application/x-www-form-urlencoded"
    },
    data={
        "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
        "apikey": ORCHESTRATE_IAM_APIKEY
    }
)

access_token = iam_response.json()["access_token"]

# Step 2: Discover agents
endpoint = f"{ORCHESTRATE_URL}/v1/orchestrate/A2A"

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

payload = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "agents/get"
}

response = requests.post(endpoint, headers=headers, json=payload)

print("Status Code:", response.status_code)
print(response.text)