import time

class Consumer(object):
    def __init__(self, consumeInterval):
        self.consumeInterval = consumeInterval

    def process(self, flag, lock):
        while True:
            time.sleep(self.consumeInterval)
            with lock:
                flag.value += 1
                print('from consumer: ', flag.value)