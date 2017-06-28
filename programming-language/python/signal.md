# signal module

## handling Ctrl-C


```
#!/usr/bin/env python
import signal
import sys
def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C')
signal.pause()
```

https://stackoverflow.com/questions/1112343/how-do-i-capture-sigint-in-python
