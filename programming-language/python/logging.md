# logging


## configure

```
logging.basicConfig()
```

## Using config file to configure the logging behavior.

See the [example](https://github.com/benquike/fuzzer/commit/955d5c29ebbd54e0290d775962f7f369d413261f)

Code

```
import logging.config
logging.config.fileConfig(os.path.join(os.getcwd(), args.logcfg))
```

Configure examle:
```
[loggers]
keys=root,fuzzer.fuzzer

[logger_root]
level=DEBUG
handlers=hand01

[logger_fuzzer.fuzzer]
level=DEBUG
handlers=hand01
qualname=fuzzer.fuzzer

# [logger_simuvex]
# level=DEBUG
# handlers=hand01
# qualname=simuvex

[handlers]
keys=hand01

[handler_hand01]
class=StreamHandler
level=NOTSET
formatter=form01
args=(sys.stdout,)

[formatters]
keys=form01

[formatter_form01]
format=F1 %(asctime)s %(levelname)s %(message)s
datefmt=
class=logging.Formatter
```
