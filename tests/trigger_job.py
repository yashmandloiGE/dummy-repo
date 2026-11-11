import base64
import urllib.request
import urllib.error

# Jenkins Configuration
JENKINS_URL = "http://localhost:8080"
JOB_NAME = "Jenkins-job"
JOB_TOKEN = "MY_SECRET_TOKEN"  # Token set in Job Configuration
USER_NAME = "admin"            # Your Jenkins username
API_TOKEN = "110a012c323e1c1dabf5bbdbcd45562e58"  # API Token generated in Step 2

# Construct Jenkins REST API endpoint
url = f"{JENKINS_URL}/job/{JOB_NAME}/build?token={JOB_TOKEN}"

# Set up HTTP POST Request with Basic Authentication
request = urllib.request.Request(url, method="POST")
credentials = f"{USER_NAME}:{API_TOKEN}"
encoded_credentials = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")
request.add_header("Authorization", f"Basic {encoded_credentials}")

print(f"Sending remote trigger request to Jenkins for job '{JOB_NAME}'...")

try:
    with urllib.request.urlopen(request) as response:
        if response.status in (200, 201):
            print("SUCCESS: Jenkins job triggered successfully!")
            print(f"Build queued at: {response.headers.get('Location', 'Queue endpoint')}")
        else:
            print(f"Trigger sent with response status: {response.status}")
except urllib.error.HTTPError as e:
    print(f"ERROR: Failed to trigger Jenkins job. Status Code: {e.code}")
    print(f"Reason: {e.reason}")
except Exception as e:
    print(f"ERROR: Could not connect to Jenkins: {e}")