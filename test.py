#coding:utf-8
import random
from mq import MessageQueue

addr = {
    "host":"127.0.0.1",
    "port":6379,
    "queue":'queue',
}

def test_timeout():
    r.rpush('rfyiamcool@163.com',timeout=5)

def test_only():
    r.rpush('http://github.com/rfyiamcool')

def test_commit():
    r.rpush('xiaorui.cc',timeout=5)
    r.commit('xiaorui.cc')
    
def test_performance():
    for i in range(10000):
        r.rpush(random.randrange(1,10000),timeout=10)
    
r = MessageQueue(**addr)

if __name__ == "__main__":
    test_only()
    test_commit()
    test_timeout()
    test_performance()
    print 'end...'
