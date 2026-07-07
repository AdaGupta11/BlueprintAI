import uuid
import requests

from config import ORCHESTRATE_IAM_APIKEY

# Get IAM Token
iam_url = "https://iam.cloud.ibm.com/identity/token"

token_response = requests.post(
    iam_url,
    headers={
        "Content-Type": "application/x-www-form-urlencoded"
    },
    data={
        "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
        "apikey": ORCHESTRATE_IAM_APIKEY
    }
)

access_token = token_response.json()["access_token"]

# Your BlueprintAI agent URL
agent_url = "https://api.us-south.watson-orchestrate.cloud.ibm.com/instances/7b5f5ee4-0706-4090-9ffc-8768ddc064ef/v1/orchestrate/A2A/agents/86a68bd2-f332-48d6-ad2c-ec3df3e31e2d/environment/0d5bd3ed-e33e-44b9-900f-29ec0e945228"

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

payload = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "message/send",
    "params": {
        "message": {
            "messageId": str(uuid.uuid4()),
            "role": "user",
            "parts": [
                {
                    "kind": "text",
                    "text": "Generate a startup blueprint for an AI-powered hostel management platform."
                }
            ]
        }
    }
}

response = requests.post(agent_url, headers=headers, json=payload)

print("Status Code:", response.status_code)
print(response.text)