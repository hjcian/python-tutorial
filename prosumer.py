import threading
import queue
import time
import datetime

def produce(q):
    print("Start loop produce")
    while True:
        time.sleep(1)
        job = datetime.datetime.now()
        print("put the job: ", job)
        q.put(job)

def consume(q):
    print("Start loop consume")
    while True:
        time.sleep(3)
        while q.qsize():
            job = q.get() # will block until has the job
            print("do the job:", job)

if __name__ == "__main__":
    jobs = queue.Queue() # 資料通道
    
    t1 = threading.Thread(target=produce, args=(jobs,))
    t2 = threading.Thread(target=consume, args=(jobs,))
    t1.start()
    t2.start()
