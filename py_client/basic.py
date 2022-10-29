import requests

# endpoint = "https://httpbin.org/status/200"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api/"


get_response = requests.post(endpoint, json={"product_id":123 }) # HTTP Request
# print(get_response.text) # print raw text response code
# print(get_response.status_code)

print(get_response.json())
# print(get_response.status_code)
