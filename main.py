from multiprocessing import Process, Value, Lock
from Consumer import Consumer
from ConsumeChecker import ConsumeChecker


if __name__ == '__main__':
    flag = Value('i', 0)
    lock = Lock()
    consumer = Consumer(.5)
    consumeProcess = Process(target = consumer.process, args = (flag, lock))
    checker = ConsumeChecker(2)
    checkProcess = Process(target = checker.make_check, args = (flag, lock))
    consumeProcess.start()
    checkProcess.start()
    consumeProcess.join()
    checkProcess.join()
    print('main thread end')