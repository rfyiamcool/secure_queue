#coding:utf-8
import time
import redis

from utils import get_time

class MessageQueue(object):

    def __init__(self, host, port, queue='queue'):
        self._conn = redis.Redis(connection_pool=redis.BlockingConnectionPool(max_connections=15, host=host, port=port))
        self.set_queue(queue)

    def set_queue(self, queue):
        self.queue = queue
        self.ack_queue = "ack_%s"%queue

    def rpush(self, msg, timeout=0):
        self._conn.rpush(self.queue, msg)
        if timeout:
            self.zadd(get_time()+timeout ,msg)
        return True
    
    def commit(self, msg):
        return self.zrem(msg)

    def lpop(self):
        msg = self._conn.lpop(self.queue)
        return msg

    def zadd(self, timestamp, value):
        return self._conn.zadd(self.ack_queue, value, timestamp)

    def zrem(self, value):
        return self._conn.zrem(self.ack_queue, value)

    def zscore(self, value):
        return self._conn.zscore(self.ack_queue, value)

    def zrangebyscore(self):
        res = self._conn.zrangebyscore(self.ack_queue , 0, get_time())
        if not isinstance(res,list):
            res = [res]
        return res

    def sadd(self, queue, value):
        return self._conn.sadd(queue, value)

    def spop(self, queue):
        msg = self._conn.spop(queue)
        return msg if msg else msg

    def srem(self, queue, value):
        return self._conn.srem(queue, value)


if __name__ == "__main__":
    addr = {
        "host":"127.0.0.1",
        "port":6379,
        "queue":'queue',
    }
    
    r = MessageQueue(**addr)
