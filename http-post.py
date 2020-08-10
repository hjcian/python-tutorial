import requests
import json

url = "http://httpbin.org/post"
headers = {
    "content-type": "application/json"
}
payload = {
    "foo": "bar",
    "hello": "world",
    "dataarray": [ 1, 2, 3 ]
}

resp = requests.post(url, json=payload, headers=headers)

# Show the Request content
print("[Our request header]")
print(json.dumps(dict(resp.request.headers), indent=4), "\n")

print("[Our request body]")
print(resp.request.body, "\n")

print("="*50)
# Show the Response content
print("[Server responded status]")
print(resp.status_code, "\n")

print("[Server responded headers]")
print(json.dumps(dict(resp.headers), indent=4), "\n")

print("[Server responded body]")
print(resp.text, "\n")