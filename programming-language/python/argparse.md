# argparse module

This module is used for parsing argumnets[^1][^2].

```
add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])
```

## Usage example


```
import argparse.ArgumentParser(usage='.....')

parser = argparse.Args

parser.add_argument("--bin_path", required=True, help="The path to the binary to run")
parser.add_argument("--input_dir", required=True, help="The directory containing all the inputs")
parser.add_argument("--cov_dir", help="The directory to put the coverage info files")

args = parser.parse_args()

# use args.

args.bin_path...

```

## bool switches

```
parser.add_argument('-b', action='store_true', default=False)
```

## parsing lists of values

`nargs`: '+' for one or more values, '*' for 0 or more values[^3].

## allowing specific values

https://stackoverflow.com/questions/15836713/allowing-a-specific-value-for-an-argparse-argument

```
...
parser.add_argument('--val', dest='val', action='store',
                      choices=['a','b','c'],
                                            help='Special testing value')

args = parser.parse_args(sys.argv[1:])
```

## Reference
[^1]: https://docs.python.org/3/library/argparse.html
[^2]: http://songpengfei.iteye.com/blog/1320877
[^3]: https://stackoverflow.com/questions/15753701/argparse-option-for-passing-a-list-as-option
