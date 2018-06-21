# Shell Programming

## sequence expression

### using range expression
```
for i in {1..5}; do echo $i; done
```

### using `seq` command

```
for i in $(seq 1 $END); do echo $i; done
```

## Loop using iteration

```
END=5
for ((i=1;i<=END;i++)); do
    echo $i
done
```

or

```
limit=4

i=1; while [ $i -le $limit ]; do
  echo $i
  i=$(($i + 1))
done
```

## arrays

```
  ${arr[*]}         # All of the items in the array
  ${!arr[*]}        # All of the indexes in the array
  ${#arr[*]}        # Number of items in the array
  ${#arr[0]}        # Length of item zero
```


## getopt

if we want an option to take an argument, then we can add `:` in the optstr,
example:

```
#!/bin/sh

# A POSIX variable
OPTIND=1         # Reset in case getopts has been used previously in the shell.

# Initialize our own variables:
output_file=""
verbose=0

while getopts "h?vf:" opt; do
    case "$opt" in
    h|\?)
        show_help
        exit 0
        ;;
    v)  verbose=1
        ;;
    f)  output_file=$OPTARG
        ;;
    esac
done

shift $((OPTIND-1))

[ "${1:-}" = "--" ] && shift

echo "verbose=$verbose, output_file='$output_file', Leftovers: $@"
```


## reference

1. http://www.linuxjournal.com/content/bash-arrays
2. https://stackoverflow.com/questions/192249/how-do-i-parse-command-line-arguments-in-bash
3. http://wiki.bash-hackers.org/howto/getopts_tutorial
4. http://wiki.bash-hackers.org/scripting/posparams