import threading


class Counter():
    def __init__(self):
        self.a = 0

    def getCount(self):
        self.a += 1
        return self.a


if __name__ == "__main__":
    counter = Counter()

    num_thread = 10000

    threads = [
        threading.Thread(target=counter.getCount)
        for i in range(num_thread)
        ]

    [thread.start() for thread in threads]

    [thread.join() for thread in threads]
    print(f"Expect a is {num_thread}, we will get {counter.a} because the GIL")
    print("Expect a is {1}, we will get {0} because the GIL".format(
        num_thread,
        counter.a))
