import json

# 1. We mimic the network response using a raw text string
mock_web_response = '{"iss_position": {"latitude": "-41.134", "longitude": "164.201"}, "message": "success"}'

# 2. Convert the text string into a clean Python Dictionary
data = json.loads(mock_web_response)

# 3. Pull data out cleanly using keys
print(f"??? The ISS is currently at Latitude: {data['iss_position']['latitude']}, Longitude: {data['iss_position']['longitude']}")
