import time
import requests
import threading

def sendRequest(url):
    start = time.time()
    resp = requests.get(url)
    diff = time.time() - start
    print("consume {:.2f} s on {}".format(diff, url))

if __name__ == "__main__":

    start = time.time()

    t1 = threading.Thread(target=sendRequest, args=("https://example.com",))
    t2 = threading.Thread(target=sendRequest, args=("https://www.google.com",))
    t3 = threading.Thread(target=sendRequest, args=("https://www.apple.com",))

    t1.start() # start a new thread
    t2.start() # start a new thread
    t3.start() # start a new thread

    t1.join() # 告知 main thread 要等這條 thread 做完才能執行下一行
    t2.join() # 告知 main thread 要等這條 thread 做完才能執行下一行
    t3.join() # 告知 main thread 要等這條 thread 做完才能執行下一行

    diff = time.time() - start
    print("Total time: {:.2f} s".format(diff))
