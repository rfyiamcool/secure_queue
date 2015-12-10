#coding=utf-8
import time
from mq import MessageQueue
from threading import Thread, Lock

from utils import get_time

addr = {
    "host":"127.0.0.1",
    "port":6379,
}

r = MessageQueue(**addr)

class SchedulerWorker(object):

    def __init__(self,queue, thread_num=5):
        queue = 'queue'
        r.set_queue(queue)
        self.mutex= Lock()
        self.thread_num = thread_num

    def run(self):
        self.spawn_worker()

    def spawn_worker(self):
        t_list = []
        for th_i in range(self.thread_num):
            t_threading = Thread(target=self.spawn_run,args=())
            t_list.append(t_threading)

        for th_i in t_list:
            th_i.start()

    def spawn_run(self):
        while True:
            if self.mutex.acquire(1):
                res = r.zrangebyscore()
                for i in res:
                    r.zrem(i)
                    r.rpush(i)
                self.mutex.release()
            time.sleep(0.1)

if __name__ == '__main__':
    queue = 'queue'
    scheduler = SchedulerWorker(queue)
    scheduler.run()
