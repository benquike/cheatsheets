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

## reference

1. http://www.linuxjournal.com/content/bash-arrays
