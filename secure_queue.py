#coding=utf-8
import time
from mq import MessageQueue
from threading import Thread, Lock

from utils import get_time
from log import get_logger

addr = {
    "host":"127.0.0.1",
    "port":6379,
}

r = MessageQueue(**addr)
logger = get_logger('debug.log')

class SchedulerWorker(object):

    def __init__(self,queue, thread_num=5):
        r.set_queue(queue)
        self.mutex= Lock()
        self.thread_num = thread_num

    def run(self):
        self.spawn_worker()

    def spawn_worker(self):
        t_list = []
        for th_i in range(self.thread_num):
            t_threading = Thread(target=self.spawn_handler,args=())
            t_list.append(t_threading)

        for th_i in t_list:
            th_i.start()

    def spawn_handler(self):
        while True:
            if self.mutex.acquire(1):
                res = r.zrangebyscore()
                for i in res:
                    logger.info(i)
                    r.zrem(i)
                    r.rpush(i[:-32])
                self.mutex.release()
            time.sleep(0.1)

if __name__ == '__main__':
    queue = 'queue'
    scheduler = SchedulerWorker(queue)
    scheduler.run()
