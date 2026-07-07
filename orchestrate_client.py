"""
BlueprintAI - IBM Watson Orchestrate Client

This module handles:
- IBM Cloud IAM authentication
- Sending startup prompts to IBM Watson Orchestrate
- Receiving and parsing the generated startup blueprint
"""

import json
import uuid
import requests

from config import ORCHESTRATE_IAM_APIKEY


# IBM Watson Orchestrate Agent Endpoint
AGENT_URL = (
    "https://api.us-south.watson-orchestrate.cloud.ibm.com/"
    "instances/7b5f5ee4-0706-4090-9ffc-8768ddc064ef/"
    "v1/orchestrate/A2A/agents/"
    "86a68bd2-f332-48d6-ad2c-ec3df3e31e2d/"
    "environment/0d5bd3ed-e33e-44b9-900f-29ec0e945228"
)


def generate_blueprint(prompt):
    """
    Sends the startup prompt to IBM Watson Orchestrate
    and returns the generated startup blueprint.
    """

    # -------------------------
    # Get IAM Access Token
    # -------------------------

    try:

        token_response = requests.post(
            "https://iam.cloud.ibm.com/identity/token",
            headers={
                "Content-Type": "application/x-www-form-urlencoded"
            },
            data={
                "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
                "apikey": ORCHESTRATE_IAM_APIKEY
            },
            timeout=30
        )

    except requests.exceptions.RequestException as e:
        return f"Connection Error while obtaining IAM Token:\n\n{e}"

    if token_response.status_code != 200:
        return f"Failed to obtain IAM Token:\n\n{token_response.text}"

    access_token = token_response.json()["access_token"]

    # -------------------------
    # Request Headers
    # -------------------------

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    # -------------------------
    # Request Payload
    # -------------------------

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
                        "text": prompt
                    }
                ]
            }
        }
    }

    # -------------------------
    # Send Request
    # -------------------------

    try:

        response = requests.post(
            AGENT_URL,
            headers=headers,
            json=payload,
            timeout=60
        )

    except requests.exceptions.RequestException as e:
        return f"Connection Error while contacting BlueprintAI Agent:\n\n{e}"

    if response.status_code != 200:
        return f"Request Failed:\n\n{response.text}"

    # -------------------------
    # Parse Response
    # -------------------------

    try:

        data = response.json()

        result = data.get("result", {})

        # Latest Watson Orchestrate response format
        if "parts" in result and len(result["parts"]) > 0:
            return result["parts"][0].get(
                "text",
                "No blueprint was returned."
            )

        # Older Watson Orchestrate response format
        if "history" in result and len(result["history"]) > 0:
            return result["history"][-1]["parts"][0].get(
                "text",
                "No blueprint was returned."
            )

        # Fallback (useful for debugging unknown response formats)
        return json.dumps(data, indent=2)

    except Exception as e:
        return (
            f"Parsing Error:\n\n{e}\n\n"
            f"Response:\n\n{response.text}"
        )