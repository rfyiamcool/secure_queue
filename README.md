# secure_queue

一句话，secure_queue可以让redis支持ACK(消息确认)

很喜欢使用redis做MQ消息队列, 使用他的List类型结构实现队列, 简单高效性能极好的优点, 但是相比rabbitmq、kafka又没有消息确认的特性. 那么我通过实现一个服务来扩展redis的消息确认功能. 

secure_queue主要分两部分:  

* secure_queue client

每次消费队列的时候，会往该队列的ack_queue有序队列扔任务, score为任务的最长超时时间.

* secure_queue.py

用来维护ack_queue, 把符合条件的任务重新扔回任务队列


Future:  
1. redis zset的value不能重复,解决方法在value加入uuid

##使用方法:

启动redis
```
redis-server
```

启动secure_queue服务端
```
start_secure_queue.py
```

secure_queue的客户端测试代码
```
#coding:utf-8
import random
from mq import MessageQueue

addr = {
    "host":"127.0.0.1",
    "port":6379,
    "queue":'queue', #队列名字
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
```

##性能测试
secure_queue本身没什么性能损耗，简单的暴力的测试一秒钟可以处理1w+的任务
