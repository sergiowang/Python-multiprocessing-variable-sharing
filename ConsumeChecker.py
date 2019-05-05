import time

class ConsumeChecker(object):
    def __init__(self, checkInterval):
        self.checkInterval = checkInterval
    
    def make_check(self, flag, lock):
        while True:
            time.sleep(self.checkInterval)
            with lock:
                print('from check: ', flag.value)
