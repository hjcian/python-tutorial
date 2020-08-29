import time
import requests

def sendRequest(url):
    start = time.time()
    resp = requests.get(url)
    diff = time.time() - start
    print("consume {:.2f} s on {}".format(diff, url))

if __name__ == "__main__":
    start = time.time()

    sendRequest("https://example.com")
    sendRequest("https://www.google.com")
    sendRequest("https://www.apple.com")

    diff = time.time() - start
    print("Total time: {:.2f} s".format(diff))
