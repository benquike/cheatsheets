# logging


## configure

```
logging.basicConfig()
```

## APIs

### writting log

```
logging.debug(msg[, *args[, **kwargs]])

logging.info(msg[, *args[, **kwargs]])

logging.warning(msg[, *args[, **kwargs]])

logging.error(msg[, *args[, **kwargs]])

logging.critical(msg[, *args[, **kwargs]])

logging.exception(msg[, *args[, **kwargs]])

```

## Formatter

configurable fields: https://docs.python.org/2/library/logging.html#logrecord-attributes

## Filter

## LoggerAdapter

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


## logging formatters


%(pathname)s Full pathname of the source file where the logging call was issued(if available).

%(filename)s Filename portion of pathname.

%(module)s Module (name portion of filename).

%(funcName)s Name of function containing the logging call.

%(lineno)d Source line number where the logging call was issued (if available).

```
formatter = logging.Formatter('[%(asctime)s] p%(process)s {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s','%m-%d %H:%M:%S')
```
