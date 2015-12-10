# secure_queue

一句话，secure_queue可以让redis支持ACK(消息确认)

很喜欢使用redis做MQ消息队列, 使用他的List类型结构实现队列, 简单高效性能极好的优点, 但是相比rabbitmq、kafka又没有消息确认的特性. 那么我通过实现一个服务来扩展redis的消息确认功能. 

* secure_queue client

每次消费队列的时候，会往该队列的ack_queue有序队列扔任务, score为任务的最长超时时间.

* secure_queue.py
用来维护ack_queue, 把符合条件的任务重新扔回任务队列

代码还没有构造完毕，写完了再补充下文档
