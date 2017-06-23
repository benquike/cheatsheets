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

## Reference
[^1]: https://docs.python.org/3/library/argparse.html
[^2]: http://songpengfei.iteye.com/blog/1320877
