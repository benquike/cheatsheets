# celery config


## installing broker

It supports various brokers. here we use rabbitmq.


## using celery over rabbitmq

1. Define a task as follows:

The important part is in the `broker` argument.
Save this file in `tasks.py`

```
from celery import Celery

app = Celery('tasks', broker='pyamqp://')

@app.task
def add(x, y):
        return x + y
```


2. start a work server

```
celery -A tasks worker --loglevel=info

-------------- celery@hexfuzz-node02 v4.0.2 (latentcall)
---- **** ----- 
--- * ***  * -- Linux-4.4.0-78-generic-x86_64-with-Ubuntu-16.04-xenial 2017-06-22 12:03:31
-- * - **** --- 
- ** ---------- [config]
- ** ---------- .> app:         tasks:0x7f9409e07950
- ** ---------- .> transport:   amqp://guest:**@localhost:5672//
- ** ---------- .> results:     disabled://
- *** --- * --- .> concurrency: 8 (prefork)
-- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
--- ***** ----- 
 -------------- [queues]
                .> celery           exchange=celery(direct) key=celery
                

[tasks]
  . tasks.add

[2017-06-22 12:03:32,082: INFO/MainProcess] Connected to amqp://guest:**@127.0.0.1:5672//
[2017-06-22 12:03:32,088: INFO/MainProcess] mingle: searching for neighbors
[2017-06-22 12:03:33,109: INFO/MainProcess] mingle: all alone
[2017-06-22 12:03:33,131: INFO/MainProcess] celery@hexfuzz-node02 ready
```

3. run a task from another node

copy the `tasks.py` to another node and run the following code
in ipython.

```
In [1]: from tasks import add

In [2]: result = add.delay(4, 4)

```
As the second command finishes, the console on the node running work server
outputs the following message:

```
[2017-06-22 12:04:45,740: INFO/MainProcess] Received task: tasks.add[8a6450a7-ac68-466c-b2f3-12c8036e5e61]  
[2017-06-22 12:04:47,165: INFO/PoolWorker-1] Task tasks.add[8a6450a7-ac68-466c-b2f3-12c8036e5e61] succeeded in 0.000310328323394s: 8
```

## celery configuration

http://docs.celeryproject.org/en/latest/userguide/configuration.html#configuration


## tasks

### periodic tasks

http://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html




## workers


## flower plugin

## monitoring and admin by cmd

### list workers

```
celery -A proj status
```

Ref: http://docs.celeryproject.org/en/latest/userguide/monitoring.html


### inspecting a live app


```
celery -A driller_mng shell
```

will start an ipython shell in which we can
inspect the app

```
import driller_mng
# get the app instance
app = driller_mng.celery_app

# gen an inspect object
i = app.control.inspect()

# from this object, we can get a lot of information
# about the app

## this method returns all the active tasks
print(i.active())

```
