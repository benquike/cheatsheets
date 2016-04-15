# default variable in perl

## $_
`$_` [^1]is the default variable in perl, which sevaral functions and operators uses by default,
if their arguments are not specified, that is to say, you do not need to write it explicitly.

e.g 
```
use strict;
use warnings;
use v5.10;

while (<STDIN>) {
    chomp;
    if (/MATCH/) {
        say;
    }
}
```

is actually the same as:

```
use strict;
use warnings;
use v5.10;

while (S_ = <STDIN>) {
    chomp $_;
    if (S_ =~ /MATCH/) {
        say $_;
    }
}
```

[^1]: http://perlmaven.com/the-default-variable-of-perl
