# secure_queue

很喜欢使用redis做MQ消息队列,但是相比rabbitmq、kafka又没有消息确认的特性. 那么我通过一个服务来扩展redis的消息确认功能. 

1. python secure_queue

每次消费队列的时候，会往一个ack_queue有序队列扔任务

2. secure_queue.py
用来维护ack_queue

代码还没有构造完毕，写完了再补充下文档
