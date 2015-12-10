#coding:utf-8
if __name__ == "__main__":
    queue = 'queue'
    ack_queue = "ack_%s"%queue
    r.zadd(ack_queue,"1xiaorui.cc",int(time.time()))
    time.sleep(1)
    res = r._conn.zrangebyscore(ack_queue,0,int(time.time()))

