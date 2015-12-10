#coding:utf-8
import time
import redis

from utils import get_time

class MessageQueue(object):

    def __init__(self, host, port):
        self._conn = redis.Redis(connection_pool=redis.BlockingConnectionPool(max_connections=15, host=host, port=port))

    def rpush(self, queue, msg):
        self._conn.rpush(queue, msg)

    def lpop(self, queue):
        msg = self._conn.spop(queue)
        return msg if msg else msg

    def popright(self, queue):
        msg = self._conn.rpop(queue)
        return msg if msg else msg

    def zadd(self, queue, timestamp, value):
        return self._conn.zadd(queue, timestamp, value)

    def zrem(self, queue, value):
        return self._conn.zrem(queue, value)

    def zscore(self, value):
        return self._conn.zscore(self.ack_queue, value)

    def zrangebyscore(self, queue):
        res = self._conn.zrangebyscore(queue , 0, get_time())
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
    pass
