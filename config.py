"""
BlueprintAI Configuration

Loads environment variables required for connecting
to IBM Watson Orchestrate.
"""

import os
from dotenv import load_dotenv


# Load environment variables from the .env file
load_dotenv()


# IBM Watson Orchestrate Credentials
ORCHESTRATE_APIKEY = os.getenv("ORCHESTRATE_APIKEY")
ORCHESTRATE_IAM_APIKEY = os.getenv("ORCHESTRATE_IAM_APIKEY")
ORCHESTRATE_URL = os.getenv("ORCHESTRATE_URL")
ORCHESTRATE_AUTH_TYPE = os.getenv("ORCHESTRATE_AUTH_TYPE")