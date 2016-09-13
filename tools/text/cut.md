# cut usage

cut can be used to select only part of each line from a file.

## format

    cut <selection>  file

### selection

1. select by bytes: `-b<range>` would select only the bytes specified by <range> of each line
2. select by character: `-c<range>` would only select the chars specified by <range> of each line
3. select by field, `-d<sep> -f<range>` would only select the fields specified <range> of each line

### range

    N      N'th byte, character or field, counted from 1
    N-     from N'th byte, character or field, to end of line
    N-M    from N'th to M'th (included) byte, character or field
    -M     from first to M'th (included) byte, character or field


### example


    $ cat file
    abcdefgh
    $ cut -b1-3 file  # only select byte1 ~ byte3
    abc

    $ cat file
    a:b:c:d:e
    $ cut -d":" -f3-
    c:d:e
