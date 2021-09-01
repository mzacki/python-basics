import json
import requests
from requests import codes
from edu.ant.tools.tester.properties import get_properties

# test case for sample api
# api call
url = get_properties().get("api_1").get("host")
key = get_properties().get("api_1").get("key")
response = requests.get(url)

# print for dev only
print(response)
response_body = (json.dumps(response.json()))
# print for dev only
print(response_body)

# given
expected_value = json.loads(response_body)
timestep = (expected_value["data"]["timelines"][0]["timestep"])

# assert
assert response.status_code == codes.ok
assert timestep == "1h"
