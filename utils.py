#coding=utf-8
import time
import uuid

def get_time():
    return int(time.time())

def get_uuid():
    return uuid.uuid4().hex

