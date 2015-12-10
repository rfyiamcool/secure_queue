#coding:utf-8
import time
import random

from mq import MessageQueue

addr = {
    "host":"127.0.0.1",
    "port":6379,
}

r = MessageQueue(**addr)

def random_str(num):
    randomlength=num
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    _random = random.Random()
    for i in range(randomlength):
        str+=chars[_random.randint(0, length)]
    return str

if __name__ == "__main__":
    queue = 'queue'
    ack_queue = "ack_%s"%queue
    for _i in range(100):
        r.zadd(ack_queue,random_str(10),int(time.time()))
        time.sleep(0.1)
    res = r._conn.zrangebyscore(ack_queue,0,int(time.time()))
    print res

