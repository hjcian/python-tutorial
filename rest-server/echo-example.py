import requests
import json

if __name__ == "__main__":
    resp = requests.get(
        "http://httpbin.org/get?key=value&haha=point",
        headers={
            "X-TEST": "Max cian"
        }
        )

    print(json.dumps(resp.json(), indent=4))
